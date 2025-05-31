from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.timezone import now
from django.db.models.functions import TruncMonth
from django.db.models import Count

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from meals.models import Meal, MealIngredient, ServedMeal
from inventory.models import Ingredient

@login_required
def serve_meal_view(request):
    if request.method == 'POST':
        meal_id = request.POST.get('meal_id')
        meal = Meal.objects.get(id=meal_id)
        ingredients_needed = MealIngredient.objects.filter(meal=meal)

        for item in ingredients_needed:
            if item.ingredient.quantity < item.quantity_required:
                messages.error(request, f"Insufficient {item.ingredient.name}")
                return redirect('serve-meal')

        for item in ingredients_needed:
            item.ingredient.quantity -= item.quantity_required
            item.ingredient.save()

        ServedMeal.objects.create(
            meal=meal,
            served_by=request.user,
            served_at=now(),
            success=True
        )
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'inventory',
            {
                'type': 'inventory_update',
                'message': 'Inventory updated after serving meal.'
            }
        )
        messages.success(request, f"{meal.name} served successfully!")
        return redirect('serve-meal')

    meals = Meal.objects.all()
    return render(request, 'meals/serve.html', {'meals': meals})

@login_required
def portion_estimate_view(request):
    meals = Meal.objects.all()
    estimates = {}

    for meal in meals:
        ingredients = MealIngredient.objects.filter(meal=meal)
        portions = []

        for item in ingredients:
            if item.quantity_required == 0:
                portions.append(0)
            else:
                portions.append(item.ingredient.quantity // item.quantity_required)

        if portions:
            estimates[meal.name] = int(min(portions))
        else:
            estimates[meal.name] = 0

    return render(request, 'meals/portions.html', {'estimates': estimates})

@login_required
def chart_view(request):
    data = (
        ServedMeal.objects
        .annotate(month=TruncMonth('served_at'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )
    chart_data = {
        'labels': [d['month'].strftime('%B %Y') for d in data],
        'values': [d['count'] for d in data],
    }
    return render(request, 'reports/chart.html', {'chart_data': chart_data})

@login_required
def dashboard_view(request):
    return render(request, 'admin/dashboard.html')

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    return render(request, "config/dashboard.html")

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def meal_create_view(request):
    return render(request, "config/meal_create.html")

@login_required
def meal_update_view(request, meal_id=None):
    return render(request, "config/meal_update.html", {"meal_id": meal_id})

@login_required
def meal_delete_view(request, meal_id=None):
    return render(request, "config/meal_delete.html", {"meal_id": meal_id})

from meals.forms import MealForm

@login_required
def meal_create_view(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meal-list')
    else:
        form = MealForm()
    return render(request, "config/meal_create.html", {"form": form})

@login_required
def meal_update_view(request, meal_id=None):
    meal = get_object_or_404(Meal, id=meal_id)
    if request.method == 'POST':
        form = MealForm(request.POST, instance=meal)
        if form.is_valid():
            form.save()
            return redirect('meal-list')
    else:
        form = MealForm(instance=meal)
    return render(request, "config/meal_update.html", {"form": form, "meal": meal})

@login_required
def meal_delete_view(request, meal_id=None):
    meal = get_object_or_404(Meal, id=meal_id)
    if request.method == 'POST':
        meal.delete()
        return redirect('meal-list')
    return render(request, "config/meal_delete.html", {"meal": meal})

from inventory.forms import IngredientForm
from inventory.models import Ingredient

@login_required
def ingredient_list_view(request):
    ingredients = Ingredient.objects.all()
    return render(request, "config/ingredient_list.html", {"ingredients": ingredients})

@login_required
def ingredient_create_view(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredient-list')
    else:
        form = IngredientForm()
    return render(request, "config/ingredient_create.html", {"form": form})

@login_required
def ingredient_update_view(request, ingredient_id=None):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('ingredient-list')
    else:
        form = IngredientForm(instance=ingredient)
    return render(request, "config/ingredient_update.html", {"form": form, "ingredient": ingredient})

@login_required
def ingredient_delete_view(request, ingredient_id=None):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    if request.method == 'POST':
        ingredient.delete()
        return redirect('ingredient-list')
    return render(request, "config/ingredient_delete.html", {"ingredient": ingredient})

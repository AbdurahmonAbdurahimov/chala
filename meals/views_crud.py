from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from meals.models import Meal
from meals.forms import MealForm

@login_required
def meal_list_view(request):
    meals = Meal.objects.all()
    return render(request, 'meals/meal_list.html', {'meals': meals})

@login_required
def meal_create_view(request):
    form = MealForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('meal-list')
    return render(request, 'meals/meal_form.html', {'form': form, 'form_title': 'Add Meal'})

@login_required
def meal_update_view(request, pk):
    obj = get_object_or_404(Meal, pk=pk)
    form = MealForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('meal-list')
    return render(request, 'meals/meal_form.html', {'form': form, 'form_title': 'Edit Meal'})

@login_required
def meal_delete_view(request, pk):
    obj = get_object_or_404(Meal, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('meal-list')
    return render(request, 'meals/meal_confirm_delete.html', {'object': obj})

from .models import MealIngredient
from .forms import MealIngredientForm

@login_required
def meal_ingredient_list_view(request):
    items = MealIngredient.objects.select_related('meal', 'ingredient').all()
    return render(request, 'meals/meal_ingredient_list.html', {'items': items})

@login_required
def meal_ingredient_create_view(request):
    form = MealIngredientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('meal-ingredient-list')
    return render(request, 'meals/meal_ingredient_form.html', {'form': form, 'form_title': 'Add Meal Ingredient'})

@login_required
def meal_ingredient_update_view(request, pk):
    obj = get_object_or_404(MealIngredient, pk=pk)
    form = MealIngredientForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('meal-ingredient-list')
    return render(request, 'meals/meal_ingredient_form.html', {'form': form, 'form_title': 'Edit Meal Ingredient'})

@login_required
def meal_ingredient_delete_view(request, pk):
    obj = get_object_or_404(MealIngredient, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('meal-ingredient-list')
    return render(request, 'meals/meal_ingredient_confirm_delete.html', {'object': obj})

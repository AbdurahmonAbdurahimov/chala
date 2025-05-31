from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from inventory.models import Ingredient
from inventory.forms import IngredientForm

@login_required
def ingredient_list_view(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'inventory/ingredient_list.html', {'ingredients': ingredients})

@login_required
def ingredient_add_view(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredient-list')
    else:
        form = IngredientForm()
    return render(request, 'inventory/ingredient_form.html', {'form': form, 'form_title': 'Add Ingredient'})

@login_required
def ingredient_edit_view(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('ingredient-list')
    else:
        form = IngredientForm(instance=ingredient)
    return render(request, 'inventory/ingredient_form.html', {'form': form, 'form_title': 'Edit Ingredient'})

@login_required
def ingredient_delete_view(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        ingredient.delete()
        return redirect('ingredient-list')
    return render(request, 'inventory/ingredient_form.html', {'form': None, 'form_title': f'Confirm deletion of {ingredient.name}'})
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from inventory.models import Ingredient
from django import forms

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'min_quantity']

@login_required
def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'inventory/ingredient_list.html', {'ingredients': ingredients})

@login_required
def ingredient_create(request):
    form = IngredientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ingredient-list')
    return render(request, 'inventory/form.html', {'form': form, 'form_title': 'Add Ingredient'})

@login_required
def ingredient_update(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    form = IngredientForm(request.POST or None, instance=ingredient)
    if form.is_valid():
        form.save()
        return redirect('ingredient-list')
    return render(request, 'inventory/form.html', {'form': form, 'form_title': 'Edit Ingredient'})

@login_required
def ingredient_delete(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        ingredient.delete()
        return redirect('ingredient-list')
    return render(request, 'inventory/confirm_delete.html', {'object': ingredient})
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from inventory.models import Ingredient
from inventory.forms import IngredientForm

@login_required
def ingredient_list_view(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'inventory/ingredient_list.html', {'ingredients': ingredients})

@login_required
def ingredient_create_view(request):
    form = IngredientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ingredient-list')
    return render(request, 'inventory/ingredient_form.html', {'form': form, 'form_title': 'Add Ingredient'})

@login_required
def ingredient_update_view(request, pk):
    obj = get_object_or_404(Ingredient, pk=pk)
    form = IngredientForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('ingredient-list')
    return render(request, 'inventory/ingredient_form.html', {'form': form, 'form_title': 'Edit Ingredient'})

@login_required
def ingredient_delete_view(request, pk):
    obj = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('ingredient-list')
    return render(request, 'inventory/ingredient_confirm_delete.html', {'object': obj})

from django import forms
from .models import MealIngredient

class MealIngredientForm(forms.ModelForm):
    class Meta:
        model = MealIngredient
        fields = ['meal', 'ingredient', 'quantity_required']
        widgets = {
            'meal': forms.Select(attrs={'class': 'form-select'}),
            'ingredient': forms.Select(attrs={'class': 'form-select'}),
            'quantity_required': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    
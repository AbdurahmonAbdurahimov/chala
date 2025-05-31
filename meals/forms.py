
from django import forms
from .models import Meal

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['name']  # Maydonlarni kerak bo'lsa kengaytirish mumkin

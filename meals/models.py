from django.db import models
from inventory.models import Ingredient
from django.contrib.auth import get_user_model

class Meal(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

class MealIngredient(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity_required = models.FloatField()

class ServedMeal(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    served_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    served_at = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=True)

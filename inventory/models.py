from django.db import models
from django.contrib.auth import get_user_model

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity = models.FloatField(help_text="grams")
    min_quantity = models.FloatField(default=100.0)
    delivery_date = models.DateField(null=True, blank=True)  # Qo‘shildi
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class IngredientDelivery(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()
    delivery_date = models.DateField()
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

from rest_framework import serializers
from .models import Meal, MealIngredient, ServedMeal

class MealIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealIngredient
        fields = '__all__'

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'

class ServedMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServedMeal
        fields = '__all__'

from django.contrib import admin
from .models import Meal, MealIngredient, ServedMeal

class MealIngredientInline(admin.TabularInline):
    model = MealIngredient
    extra = 1

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [MealIngredientInline]
    search_fields = ('name',)

@admin.register(ServedMeal)
class ServedMealAdmin(admin.ModelAdmin):
    list_display = ('meal', 'served_by', 'served_at', 'success')
    list_filter = ('served_at', 'served_by', 'success')
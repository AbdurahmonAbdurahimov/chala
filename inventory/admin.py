from django.contrib import admin
from .models import Ingredient, IngredientDelivery

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'min_quantity', 'updated_at')
    search_fields = ('name',)
    list_filter = ('updated_at',)
    ordering = ('name',)

@admin.register(IngredientDelivery)
class IngredientDeliveryAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'quantity', 'delivery_date', 'created_by', 'created_at')
    search_fields = ('ingredient__name',)
    list_filter = ('delivery_date', 'created_by')
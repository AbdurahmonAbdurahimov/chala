from django.urls import path

from .views import (
    ingredient_list_view,
    ingredient_create_view,
    ingredient_update_view,
    ingredient_delete_view,
    dashboard_view,
    meal_list_view,
    meal_create_view,
    meal_update_view,
    meal_delete_view,
)

urlpatterns = [
    path('ingredients/', ingredient_list_view, name='ingredient-list'),
    path('ingredients/create/', ingredient_create_view, name='ingredient-create'),
    path('ingredients/update/<int:ingredient_id>/', ingredient_update_view, name='ingredient-update'),
    path('ingredients/delete/<int:ingredient_id>/', ingredient_delete_view, name='ingredient-delete'),

    path('', dashboard_view, name='dashboard'),
    path('meals/', meal_list_view, name='meal-list'),
    path('meals/create/', meal_create_view, name='meal-create'),
    path('meals/update/<int:meal_id>/', meal_update_view, name='meal-update'),
    path('meals/delete/<int:meal_id>/', meal_delete_view, name='meal-delete'),
]

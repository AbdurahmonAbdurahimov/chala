from django.urls import path
from .views_crud import (
    meal_list_view,
    meal_create_view,
    meal_update_view,
    meal_delete_view
)

urlpatterns = [
    path('', meal_list_view, name='meal-list'),
    path('create/', meal_create_view, name='meal-create'),
    path('<int:pk>/edit/', meal_update_view, name='meal-update'),
    path('<int:pk>/delete/', meal_delete_view, name='meal-delete'),
]
from django.urls import path
from . import views_crud

urlpatterns += [
    path('meal-ingredients/', views_crud.meal_ingredient_list_view, name='meal-ingredient-list'),
    path('meal-ingredients/create/', views_crud.meal_ingredient_create_view, name='meal-ingredient-create'),
    path('meal-ingredients/<int:pk>/edit/', views_crud.meal_ingredient_update_view, name='meal-ingredient-update'),
    path('meal-ingredients/<int:pk>/delete/', views_crud.meal_ingredient_delete_view, name='meal-ingredient-delete'),
]

from django.urls import path
from .views_crud import (
    ingredient_list_view,
    ingredient_create_view,
    ingredient_update_view,
    ingredient_delete_view
)

urlpatterns = [
    path('ingredients/', ingredient_list_view, name='ingredient-list'),
    path('ingredients/create/', ingredient_create_view, name='ingredient-create'),
    path('ingredients/<int:pk>/edit/', ingredient_update_view, name='ingredient-update'),
    path('ingredients/<int:pk>/delete/', ingredient_delete_view, name='ingredient-delete'),
]
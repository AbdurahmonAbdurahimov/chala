from django.urls import path
from .views import (
    ingredient_list_view,
    ingredient_add_view,
    ingredient_edit_view,
    ingredient_delete_view
)

urlpatterns = [
    path('ingredients/', ingredient_list_view, name='ingredient-list'),
    path('ingredients/add/', ingredient_add_view, name='ingredient-add'),
    path('ingredients/edit/<int:pk>/', ingredient_edit_view, name='ingredient-edit'),
    path('ingredients/delete/<int:pk>/', ingredient_delete_view, name='ingredient-delete'),
]
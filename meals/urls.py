
from django.urls import path
from .views import view_meals

urlpatterns = [
    path('view/', view_meals),
]

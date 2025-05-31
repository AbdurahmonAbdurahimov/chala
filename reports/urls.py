
from django.urls import path
from .views import monthly_report

urlpatterns = [
    path('monthly/', monthly_report),
]

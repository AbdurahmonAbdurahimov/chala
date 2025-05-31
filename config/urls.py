
from django.contrib import admin
from django.urls import path, include
from .views import serve_meal_view, portion_estimate_view, chart_view, dashboard_view

urlpatterns = [
    path('', dashboard_view),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('inventory.urls')),
    path('api/meals/', include('meals.urls')),
    path('api/reports/', include('reports.urls')),

    # Template routes
    path('dashboard/', dashboard_view),
    path('meals/serve/', serve_meal_view),
    path('meals/portions/', portion_estimate_view),
    path('reports/charts/', chart_view),
]

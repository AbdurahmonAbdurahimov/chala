from django.contrib import admin
from django.utils.html import format_html
from django.urls import path
from django.template.response import TemplateResponse
from meals.models import ServedMeal
from inventory.models import Ingredient
from django.db.models import Count
from django.db.models.functions import TruncMonth
import datetime

class CustomAdminSite(admin.AdminSite):
    site_header = 'Kindergarten Kitchen Admin'
    site_title = 'Kindergarten System'
    index_title = 'Admin Dashboard'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard-metrics/', self.admin_view(self.dashboard_view))
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        today = datetime.date.today()
        served_today = ServedMeal.objects.filter(served_at__date=today).count()
        low_stock = Ingredient.objects.filter(quantity__lt=50).count()

        most_served = (
            ServedMeal.objects.values('meal__name')
            .annotate(total=Count('id')).order_by('-total')[:5]
        )

        monthly_data = (
            ServedMeal.objects
            .annotate(month=TruncMonth('served_at'))
            .values('month')
            .annotate(count=Count('id'))
            .order_by('month')
        )

        chart_labels = [d['month'].strftime('%b %Y') for d in monthly_data]
        chart_values = [d['count'] for d in monthly_data]

        context = dict(
            self.each_context(request),
            served_today=served_today,
            low_stock=low_stock,
            most_served=most_served,
            chart_labels=chart_labels,
            chart_values=chart_values,
        )
        return TemplateResponse(request, "admin/dashboard_metrics.html", context)

admin_site = CustomAdminSite(name='custom_admin')
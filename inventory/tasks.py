from celery import shared_task
from meals.models import ServedMeal
from django.db.models.functions import TruncMonth
from django.db.models import Count

@shared_task
def generate_monthly_summary():
    data = (
        ServedMeal.objects
        .annotate(month=TruncMonth('served_at'))
        .values('month')
        .annotate(total=Count('id'))
        .order_by('month')
    )
    print("📊 Oylik ovqat berish hisobotlari:")
    for row in data:
        print(f"{row['month'].strftime('%Y-%m')}: {row['total']} ta taom xizmat ko‘rsatildi")

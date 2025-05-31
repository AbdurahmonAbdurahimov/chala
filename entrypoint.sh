#!/bin/sh

set -e

echo "📦 Running makemigrations..."
python manage.py makemigrations --noinput

echo "📦 Running migrate..."
python manage.py migrate --noinput

echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput

echo "👤 Creating superuser if not exists..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
END

echo "🚀 Starting server with: $@"
exec "$@"

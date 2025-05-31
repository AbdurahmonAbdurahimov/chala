makemigrations:
	docker-compose exec web python manage.py makemigrations

migrate: makemigrations
	docker-compose exec web python manage.py migrate

createsuperuser:
	docker-compose exec web python manage.py createsuperuser

run:
	docker-compose up --build

shell:
	docker-compose exec web python manage.py shell

logs:
	docker-compose logs -f web

celery:
	docker-compose exec celery bash

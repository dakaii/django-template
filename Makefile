.PHONY: build up down migrations migrate superuser
build:
	docker-compose build
up:
	docker-compose up && docker-compose rm -fsv
down:
	docker-compose down
migrations:
	docker-compose run web python3 manage.py makemigrations
migrate:
	docker-compose run web python3 manage.py migrate
superuser:
	docker-compose run web python3 manage.py createsuperuser




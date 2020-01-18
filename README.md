
docker-compose exec db psql --username=postgres --dbname=random_database_name
docker-compose exec web python manage.py migrate --noinput
start:
	python3 manage.py runserver

link:
	poetry run flake8

lang:
	django-admin makemessages -l ru

compile:
	django-admin compilemessages

migrate:
	python manage.py makemigrations
	python manage.py migrate
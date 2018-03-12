django-admin startproject mysite

python manage.py runserver
 http://localhost:8000/

Creating new app for personal

python manage.py startapp personal

templates used in webpages is Jinja2 and formatting is done using bootstrap


This command tells python that we have made a model and Schema change. This creates a migrations directory

python manage.py makemigrations

to check the sql that will be run for migration use: python manage.py sqlmigrate blog 0001

To start migration : python manage.py migrate

django-admin startproject mysite

python manage.py runserver
 http://localhost:8000/

Creating new app for personal

python manage.py startapp personal

templates used in webpages is Jinja2 and formatting is done using bootstrap


DATABASE :: Django handles database works with model.py ::

This command tells python that we have made a model and Schema change. This creates a migrations directory: python manage.py makemigrations

To start migration : python manage.py migrate

To check the sql that will be run for migration use: python manage.py sqlmigrate blog 0001

Creating Admin account : python manage.py createsuperuser

using https : https://pythonprogramming.net/django-web-server-https-lets-encrypt-ssl/
We will have to generate certificate using letsencrypt and disable default ports in server.

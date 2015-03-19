# DoCo Test
Primarily put together using
- Django 1.7
- Django Rest Framework
- Django-allauth
- Knockoutjs
- WhiteNoise

## API

Endpoints for resolution creation, Deletion, Updating and Listing available at

    /resolution/
    /resolution/1

## Tests

Tests are runnable using standard django practice, enhanced by nose.

python manage.py test


## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's statc file serving functionality via WhiteNoise
- Enhancements to Django's database functionality via django-postgrespool and dj-database-url

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [django-postgrespool](https://warehouse.python.org/project/django-postgrespool/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
- [django-rest-framework](http://www.django-rest-framework.org/)
- [django-allauth](http://www.intenct.nl/projects/django-allauth/)

# Salsa Lessons
An app for organizing instructors and lesson plans for the University Salsa Club at UVa's weekly practices.

## Versions
Python 3.2.5
Django 1.7
Postgres(.app) 9.3.5.1

## Commands

### Workflow

Activate virtualenv

`source env/bin/activate`

Ensure that environment variables are set correctly (see Set Up section)

Run dev server on [port] - default is 8000, admin at /admin

`python manage.py runserver <port>`

You can also use foreman, which uses the web command from the Procfile

  gunicorn mysite.wsgi
  foreman start

### Changing models

1. Change models
2. Create migrations for those changes
  `python manage.py makemigrations`
3. Apply those changes to the database
  `python manage.py migrate`

### Set Up

Ensure that environment variables are set:

	LESSONS_DB_NAME
	LESSONS_DB_USER
	LESSONS_DB_PASSWORD

Activate virtualenv

`source env/bin/activate`

Update dependencies and requirements.txt

`pip freeze > requirements.txt`

`pip install -r requirements.txt`

Create settings for environment [env]

`cp settings.py.templ setttings-[env].py`

`ln -s settings-[env].py settings.py`


Update database info and timezone

    Databases =
      'default': {
          'NAME': 'name',
          'ENGINE': 'mysql.connector.django',
          'USER': 'user',
          'PASSWORD': 'password',
          'OPTIONS': {
            'autocommit': True,
          },
      }
    }

Create superuser

`python manage.py createsuperuser`

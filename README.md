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

Ensure that environment variables are set correctly (see INSTALL.md)

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

### Deploy to Heroku

`git push heroku master`

If migrations:
`heroku run python manage.py migrate lessons

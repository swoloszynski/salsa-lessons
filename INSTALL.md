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

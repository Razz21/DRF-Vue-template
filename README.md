# Django + Vue Template

This project is broken into a Django/DRF backend and Vue frontend.

## Local setup

Clone repository:

```sh
git clone https://github.com/Razz21/DRF-Vue-template.git
```

1. Create and activate environment:

```sh
pip install virtualenvwrapper
mkvirtualenv --python=python3.7.2 venv
workon venv
```

2. Install Python dependencies:

```sh
pip install -r requirements/local.txt
python manage.py migrate
python manage.py runserver
```

Next steps require Node.js and NPM. Download and install these packages on your local machine:  
[downloading and installing Node.js and NPM](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

3. Open second terminal and run commands in repository root folder:

```sh
cd frontend
npm i
npm run serve
```

4. See the application being served through Django development server:

```
http://127.0.0.1:8000/
```

## Deployment on Heroku

Run these commands to deploy on heroku:

```sh
heroku buildpacks:set heroku/python-3.7.2
heroku buildpacks:add --index 1 heroku/nodejs

heroku addons:create heroku-postgresql:hobby-dev

heroku pg:promote DATABASE_URL

heroku config:set DJANGO_DEBUG=False

heroku config:set DJANGO_SETTINGS_MODULE=config.settings.production

heroku config:set DJANGO_SECRET_KEY="$(openssl rand -base64 64)"

# Set this to your Heroku app url
heroku config:set DJANGO_ALLOWED_HOSTS=

# -------------------------------
# add email service variables as described below
...
# -------------------------------

git push heroku master

heroku open
```

## Settings defaults

| env variable         | local defaults      | production defaults  |
| -------------------- | ------------------- | -------------------- |
| DJANGO_SECRET_KEY    | auto-generated      | raises-error         |
| DJANGO_ALLOWED_HOSTS | [*]                 | _`your-domain-name`_ |
| DJANGO_DEBUG         | True                | False                |
| DATABASE             | sqlite3             | n/a                  |
| DATABASE_URL         | n/a                 | raises-error         |
| EMAIL                | consoleEmailBackend | **Check below**      |

## Email configuration

Django-allauth setup requires email server for password reset service or email verification (optional).

Default production configuration uses smptEmailBackend and requires additional environment variables:

| env variable                | defaults                        |
| --------------------------- | ------------------------------- |
| DJANGO_EMAIL_HOST           | `smtp.gmail.com`                |
| DJANGO_EMAIL_USE_TLS        | True                            |
| DJANGO_EMAIL_PORT           | 587                             |
| DJANGO_EMAIL_HOST_USER      | none                            |
| DJANGO_EMAIL_HOST_PASSWORD  | none                            |
| DJANGO_DEFAULT_FROM_EMAIL   | _`Project noreply@example.com`_ |
| DJANGO_SERVER_EMAIL         | DEFAULT_FROM_EMAIL              |
| DJANGO_EMAIL_SUBJECT_PREFIX | _`Project`_                     |

**_check django docs for more information
https://docs.djangoproject.com/en/dev/ref/settings/_**

---

If you are willing to use API email service, like Mailgun, feel free to change email settings.  
Example settings for django-anymail(mailgun):

```diff
# requirements/production.py

+ django-anymail[mailgun]==6.0

# config/settings/production.py

- EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

- EMAIL_HOST = env("DJANGO_EMAIL_HOST")
- EMAIL_USE_TLS = env("DJANGO_EMAIL_USE_TLS", True)
- EMAIL_PORT = env("DJANGO_EMAIL_PORT", 587)
- EMAIL_HOST_USER = env("DJANGO_EMAIL_HOST_USER")
- EMAIL_HOST_PASSWORD = env("DJANGO_EMAIL_HOST_PASSWORD")

+ INSTALLED_APPS += ["anymail"]

+ EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"

+ ANYMAIL = {
+     "MAILGUN_API_KEY": env("MAILGUN_API_KEY"),
+     "MAILGUN_SENDER_DOMAIN": env("MAILGUN_DOMAIN"),
+ }
```

Then set additional env variables on Heroku:

```sh
heroku config:set MAILGUN_API_KEY=
heroku config:set MAILGUN_DOMAIN=
```

from .base import *  # noqa
from .base import env
import os

# GENERAL
# ------------------------------------------------------------------------------

SECRET_KEY = env(
    "DJANGO_SECRET_KEY", default="9f43d31e_s#)&)j-^zjz(tgwr4yj1y=npy!tz$(-&#=w8a=g7l"
)

DEBUG = env.bool("DJANGO_DEBUG", False)

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["example.com"])


# GUNICORN
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["gunicorn", "whitenoise.runserver_nostatic"]

# WHITENOISE
# ------------------------------------------------------------------------------
# http://whitenoise.evans.io/en/latest/django.html#enable-whitenoise
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

WHITENOISE_ROOT = os.path.join(FRONTEND_DIR, "dist")


# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#default-from-email
DEFAULT_FROM_EMAIL = env(
    "DJANGO_DEFAULT_FROM_EMAIL", default="Project <noreply@example.com>"
)
# https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)
# https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = env("DJANGO_EMAIL_SUBJECT_PREFIX", default="[Project]")

# EMAIL_HOST = env("DJANGO_EMAIL_HOST", 'smtp.gmail.com')
# EMAIL_USE_TLS = env("DJANGO_EMAIL_USE_TLS", True)
# EMAIL_PORT = env("DJANGO_EMAIL_PORT", 587)
# EMAIL_HOST_USER = env("DJANGO_EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = env("DJANGO_EMAIL_HOST_PASSWORD")

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"


# DATABASES
# ------------------------------------------------------------------------------
DATABASES = {}
DATABASES["default"] = env.db("DATABASE_URL")  # noqa F405
DATABASES["default"]["ATOMIC_REQUESTS"] = True  # noqa F405
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)  # noqa F405

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# STATIC
# ------------------------------------------------------------------------------

STATICFILES_STORAGE = "whitenoise.django.CompressedManifestStaticFilesStorage"


# FRONTEND
# ------------------------------------------------------------------------------
FRONTEND_URL = env("DJANGO_FRONTEND_URL", default="/")
# ACCOUNT_EMAIL_CONFIRMATION_URL = FRONTEND_URL + 'verify-email/{}'
ACCOUNT_PASSWORD_RESET_CONFIRM = FRONTEND_URL + "password/reset/confirm/"


WEBPACK_LOADER = {
    "DEFAULT": {
        "CACHE": not DEBUG,
        "BUNDLE_DIR_NAME": os.path.join(FRONTEND_DIR, "dist"),
        "STATS_FILE": os.path.join(FRONTEND_DIR, "webpack-stats-prod.json"),
    }
}


# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console", "mail_admins"],
            "propagate": True,
        },
    },
}

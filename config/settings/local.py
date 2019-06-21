from .base import *  # noqa
from .base import env

import os

# GENERAL
# ------------------------------------------------------------------------------
SECRET_KEY = "9f43d31e_s#)&)j-^zjz(tgwr4yj1y=npy!tz$(-&#=w8a=g7l"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]


# EMAIL
# ------------------------------------------------------------------------------

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# DATABASES
# ------------------------------------------------------------------------------

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(ROOT_DIR, "db.sqlite3"),
    }
}


# FRONTEND
# ------------------------------------------------------------------------------
WEBPACK_LOADER = {
    "DEFAULT": {
        "CACHE": not DEBUG,
        "BUNDLE_DIR_NAME": "/bundles/",  # must end with slash
        "STATS_FILE": os.path.join(FRONTEND_DIR, "webpack-stats.json"),
    }
}

# Vue router in hash(default) mode
# FRONTEND_URL = "http://127.0.0.1:8000/#/"

# Vue router in history mode
FRONTEND_URL = "http://127.0.0.1:8000/"

# ACCOUNT_EMAIL_CONFIRMATION_URL = FRONTEND_URL + 'verify-email/{}'
ACCOUNT_PASSWORD_RESET_CONFIRM = FRONTEND_URL + "password/reset/confirm/"

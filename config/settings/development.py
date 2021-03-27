from .base import *

# Hardcoded secret key for development only
# -------------------------------------------------------------------
SECRET_KEY = env('SECRET_KEY')
DEBUG = True
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
# -------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# URL Shortener app config
# -------------------------------------------------------------------
URL_SHORTENER_PREFIX = 'localhost:3000'
URL_SHORTENER_SALT = 3452147

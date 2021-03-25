from .base import *
import os


SECRET_KEY = env('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['zipp.link']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
# -------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD')
    }
}

# URL Shortener app config
# -------------------------------------------------------------------
URL_SHORTENER_PREFIX = 'zipp.link'
URL_SHORTENER_SALT = 3457327

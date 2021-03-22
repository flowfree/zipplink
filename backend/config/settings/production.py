import os 
from .base import *

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = [
    '50yiur6t10.execute-api.us-west-2.amazonaws.com',
    'zipp.link',
]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
# -------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD')
    }
}

# Django CORS headers
# https://github.com/adamchainz/django-cors-headers
# ------------------------------------------------------------------------
CORS_ALLOWED_ORIGINS = [
    'https://50yiur6t10.execute-api.us-west-2.amazonaws.com',
    'https://zipp.link',
    'https://api.zipp.link',
]

# URL Shortener app config
# -------------------------------------------------------------------
URL_SHORTENER_PREFIX = f'https://zipp.link'
URL_SHORTENER_SALT = 3457327

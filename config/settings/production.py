import os 
from .base import * 

SECRET_KEY = 'abcdef'
DEBUG = False
ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
# -----------------------------------------------------------------------
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

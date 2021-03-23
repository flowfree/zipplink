import os 
from .base import * 

SECRET_KEY = '12345'
DEBUG = True
ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
# -----------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
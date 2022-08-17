from recipe_django.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'SUPERSECRETAWESOMESTRING'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


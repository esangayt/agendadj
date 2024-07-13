import firebase_admin
from firebase_admin import credentials, auth

from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('APP_DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}



STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

#EMAIL SETTINGS
# EMAIL_BACKEND = config('EMAIL_BACKEND', cast=str)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_HOST = config('EMAIL_HOST', cast=str)
EMAIL_HOST_USER = config('EMAIL_USER', cast=str)
EMAIL_HOST_PASSWORD = config('EMAIL_PASSWORD',cast=str)
EMAIL_PORT = config('EMAIL_PORT', cast=int)

cred = credentials.Certificate('django-key.json')
default_app = firebase_admin.initialize_app(cred)
"""
Django settings for Charts project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import SESSION_EXPIRE_AT_BROWSER_CLOSE

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'profile'

import mimetypes
import chartkick

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'my_charts/static'),
)

########HEROKU #############
# STATIC_URL = '/static/'
# STATICFILES_DIRS = (
#     chartkick.js(),
# )


# mimetypes.add_type("image/svg+xml", ".svg", True)
# mimetypes.add_type("image/svg+xml", ".svgz", True)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3tucmz2vzt9@_o+j1vm664r&n(ae5pdub=lb!^q03)*(gdd-!s'
AUTH_USER_MODEL = 'my_charts.Player'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "my_charts/static", *MEDIA_URL.strip("/").split("/"))

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
  #  'debug_toolbar',
    'my_charts',
    'highcharts',
    'chartjs',
    'chartkick',
)

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'chintamani.lonkar@gmail.com'
EMAIL_HOST_PASSWORD = '615.Folsom'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'chintamani.lonkar@gmail.com@gmail.com'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Charts.urls'

WSGI_APPLICATION = 'Charts.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SESSION_EXPIRE_AT_BROWSER_CLOSE
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/



########HEROKU #############
# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'my_charts/templates'),
)


try:
    from local_settings import *
except ImportError:
    pass
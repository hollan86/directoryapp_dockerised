"""
Django settings for directoryapp project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '&d82uh&p3ielih9f++7*3=$i@%6v%c0j$$zi+z^s-17a_f8k#('

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '&d82uh&p3ielih9f++7*3=$i@%6v%c0j$$zi+z^s-17a_f8k#(')
# Read secret key from a file
# with open('secret_key.txt') as f:
#     SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = bool( os.environ.get('DJANGO_DEBUG', True) )

# ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ['itblogs-demo.herokuapp.com','localhost','ITblogs.es','0.0.0.0','127.0.0.1']
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',') if os.getenv('ALLOWED_HOSTS') else []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blogs',
    'podcasts',
    'rest_framework',
    'frontend',
    'tags'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'directoryapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'directoryapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.getenv('MYSQL_DATABASE'),
#         'USER': os.getenv('MYSQL_USER'),
#         'PASSWORD': os.getenv('MYSQL_PASSWORD'),
#         'HOST': os.getenv('MYSQL_HOST'),
#         'PORT': os.getenv('MYSQL_PORT')
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('EXTERNAL_MYSQL_DB'),
        'USER': os.getenv('EXTERNAL_MYSQL_USER'),
        'PASSWORD': os.getenv('EXTERNAL_MYSQL_PASSWORD'),
        'HOST': os.getenv('EXTERNAL_MYSQL_HOST'),
        'PORT': os.getenv('EXTERNAL_MYSQL_PORT')
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'OPTIONS': {
#             'read_default_file': 'myconfigurations.cnf',
#         },
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

#Deployment settings
CSRF_COOKIE_SECURE = bool( os.environ.get('CSRF_COOKIE_SECURE', False) )
SESSION_COOKIE_SECURE = bool( os.environ.get('SESSION_COOKIE_SECURE', False) )
SECURE_SSL_REDIRECT = bool( os.environ.get('SECURE_SSL_REDIRECT', False) )

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Heroku: Update database configuration from $DATABASE_URL.
# import dj_database_url
# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)

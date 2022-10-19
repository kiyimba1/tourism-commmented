"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xiy3q#=(utm4+h)ed8p2y))f6$&@ov933li86p==#8)9z82bqn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    "leaflet",
    'bootstrap5',
    'djgeojson',
    'fontawesomefree',
    'rest_framework',
    'rest_framework_gis',

    'home',
    'district',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'tourism',
        'USER': 'tourism',
        'PASSWORD': 'tourism',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_ROOT = str(BASE_DIR / "staticfiles")

STATIC_URL = '/static/'

# STATIC_FILES_DIRS = [str(BASE_DIR / 'static')]

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LEAFLET_CONFIG = {
    "TILES": [
        ("Open Street Map",
         "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {}),
        ("Google Maps",
         "http://mts3.google.com/vt/lyrs=m&x={x}&y={y}&z={z}", {}),
        ("Satellite",
         "http://mts2.google.com/vt/lyrs=y&x={x}&y={y}&z={z}", {}),
    ],

    'PLUGINS': {
        'more-markers': {
            'css': [os.path.join(STATIC_URL, ('css/leaflet.extra-markers.min.css'))],
            'js': [os.path.join(STATIC_URL, ('js/leaflet.extra-markers.min.js'))],
            'auto-include': True,
        },
        'side-bar': {
            'css': [os.path.join(STATIC_URL, ('css/leaflet-sidebar.min.css'))],
            'js': [os.path.join(STATIC_URL, ('js/leaflet-sidebar.min.js'))],
            'auto-include': True,
        },
        'locate': {
            'css': [os.path.join(STATIC_URL, ('css/L.Control.Locate.min.css')), os.path.join(STATIC_URL, ('css/L.Control.Locate.mapbox.min.css'))],
            'js': [os.path.join(STATIC_URL, ('js/L.Control.Locate.min.js'))],
            'auto-include': True,
        },
        'routing-machine': {
            'css': ["https://unpkg.com/leaflet-routing-machine@latest/dist/leaflet-routing-machine.css"],
            'js': ["https://unpkg.com/leaflet-routing-machine@latest/dist/leaflet-routing-machine.js"],
            'auto-include': True,
        }
    }
}

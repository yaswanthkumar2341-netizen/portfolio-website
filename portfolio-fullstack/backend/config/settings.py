"""
Django settings for the portfolio backend.

This powers the contact form on the portfolio site (index.html / script.js):
every submission is validated by Django REST Framework and saved to the
database, and shows up in the Django admin at /admin/.
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# --- SECURITY ---------------------------------------------------------------
# Replace this before deploying anywhere public. Keep it secret.
SECRET_KEY = 'django-insecure-change-this-key-before-deploying'

# Set to False in production.
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# --- APPS --------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',   # Django REST Framework — turns the model into an API
    'corsheaders',       # Lets the frontend (opened as a plain HTML file) call this API

    'contact',           # Our app: stores and serves contact form submissions
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',   # must sit high in the list
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
        'DIRS': [BASE_DIR / 'templates'],
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

# --- DATABASE ------------------------------------------------------------
# Default: SQLite — zero setup, a single file, perfect for running this
# locally right away.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# To switch to MySQL (matches database/schema.sql in this project):
# 1. pip install mysqlclient
# 2. create the database:  CREATE DATABASE portfolio_db;
# 3. replace the DATABASES block above with:
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'portfolio_db',
#         'USER': 'root',
#         'PASSWORD': 'your_mysql_password',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#     }
# }
#
# 4. python manage.py migrate

# --- PASSWORD VALIDATION -------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- I18N ------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# --- STATIC FILES ------------------------------------------------------------
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- CORS --------------------------------------------------------------------
# The portfolio frontend is a plain static file (opened via file:// or a
# simple dev server), so we allow it to call this API during development.
# Tighten this to your real domain before deploying.
CORS_ALLOW_ALL_ORIGINS = True

# --- DJANGO REST FRAMEWORK ---------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

"""
Django settings for djangoSite project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i!@*5*^n=*c4uw(-bcsf+t#dn()3z*%7ik-j5std&0n=0kq30x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
	'icarus',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'djangoSite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'staticDir'),
)
WSGI_APPLICATION = 'djangoSite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoDB',
	'USER': 'root',
	'PASSWORD': 'd89j92g95',
	'HOST': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/george/static/'
STATIC_ROOT = '/home/george/PersonalProjects/djangoSite/static'

LOGGING = {
   'version': 1,
   'disable_existing_loggers': True,
   'formatters': {
       'standard': {
           'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
       },
   },
   'handlers': {
       'default': {
           'level':'WARNING',
           'class':'logging.handlers.RotatingFileHandler',
           'filename': os.path.join(BASE_DIR, 'logs/mylog.log'),
           'maxBytes': 1024*1024*5, # 5 MB
           'backupCount': 5,
           'formatter':'standard',
       },  
       'request_handler': {
               'level':'DEBUG',
               'class':'logging.handlers.RotatingFileHandler',
               'filename': os.path.join(BASE_DIR, 'logs/django_request.log'),
               'maxBytes': 1024*1024*5, # 5 MB
               'backupCount': 5,
               'formatter':'standard',
       },
   },
   'loggers': {

       '': {
           'handlers': ['default'],
           'level': 'WARNING',
           'propagate': True
       },
       'django.request': {
           'handlers': ['request_handler'],
           'level': 'DEBUG',
           'propagate': False
       },
   }
}

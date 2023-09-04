"""
Django settings for conf project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

from dotenv import load_dotenv
load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-&q&8r(7rc)g$(6ua2=4!zn!cf6c#-g2js-dh!v!w^l*gf@l@m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'conf.apps.CustomAdminConfig',
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    'debug_toolbar', #debuger
    "phonenumber_field", #get phone number
    "drf_yasg",
    "admin_reorder",
    
    'shop',  #app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware', #language
    'debug_toolbar.middleware.DebugToolbarMiddleware', #debug_toolbar
    # 'admin_reorder.middleware.ModelAdminReorder', #admin_reorder
    'conf.middleware.ModelAdminReorderWithNav', #admin_reorder
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INTERNAL_IPS = [
    "127.0.0.1",
]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
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

WSGI_APPLICATION = 'conf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB'), 
        'USER': os.environ.get('POSTGRES_USER'), 
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),    
        'PORT': os.environ.get('POSTGRES_PORT')
   }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('uz', 'Uzbek'),
    ('kk', 'Cyrillic'),
    ('ru', 'Russian'),
)

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'
MODELTRANSLATION_LANGUAGES = ('uz','kk','ru')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = 'agrigate/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = [os.path.join(BASE_DIR, "staticfiles")]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media/'

ADMINS = (
    ('admin', 'jobirumirovmoliya@gmail.com'),
)

# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
#     'PAGE_SIZE': 10
# }


ADMIN_REORDER = (
    {'app': 'auth', 'label': 'Admin',
     'models': (
        {'model': 'auth.Group', 'label': 'Adminstratorlar guruhlari'},
        {'model': 'auth.User', 'label': 'Adminstratorlar'},
    )},

    {'app': 'shop', 'label': 'Bot',
     'models': ('shop.BotUser',)
    },

    {'app': 'shop', 'label': "E'lon",
     'models': ('shop.TelegramGroupChannel', 'shop.AdsUser', 'shop.AdsCategory', 'shop.Advertisement')
    },

    {'app': 'shop', 'label': 'Manba',
     'models': ('shop.UsefulCategory', 'shop.UsefulCatalog',)
    },
)

TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.filesystem.Loader',
)
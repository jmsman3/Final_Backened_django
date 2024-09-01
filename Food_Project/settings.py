"""
Django settings for Food_Project project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import dj_database_url
import environ
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-78z!c_#qn!b5hr4ehs2=d#wg54o)v4gxex+(06x-tx85fals%$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = [
    'https://food-project-9vo4.onrender.com', # Replace with your actual domain
    'http://127.0.0.1',  # Local development
     
]

# CSRF_TRUSTED_ORIGINS = [
#     # 'http://127.0.0.1:8000',
#     # 'http://localhost:8000',
    
# #    'http://127.0.0.1:8000/user/register/',
# #    'http://127.0.0.1:8000/user/login/',
# #    'http://127.0.0.1:8000/user/logout/',
# #    'http://127.0.0.1:8000/user/list/',

# #    'http://127.0.0.1:8000/menu/products/',
# #    'http://127.0.0.1:8000/order/cart',
# #    'http://127.0.0.1:8000/order/order_now',
# #    'https://food-project-9vo4.onrender.com/admin/',

#    'https://food-project-9vo4.onrender.com/user/login/',
#    'https://food-project-9vo4.onrender.com/user/logout/',
#    'https://food-project-9vo4.onrender.com/user/list/',



#    'https://food-project-9vo4.onrender.com/menu/products/',
#    'https://food-project-9vo4.onrender.com/order/cart',
#    'https://food-project-9vo4.onrender.com/order/order_now',
# ]



# Application definition


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',  #cors
    'rest_framework' ,   #rest framework
    'rest_framework.authtoken',
    'users',           # Authentication and Profiles
    'menu',            #Food menu and special
    'orders',          #Order ,cart, and reviews
    'delivery',        #delivery management thing
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  #cors
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ALLOW_ALL_ORIGINS = True  # Allow all origins to access  API

# CORS configuration

CORS_ALLOW_CREDENTIALS = True  # Allow credentials like cookies to be sent
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
]
CORS_ALLOW_HEADERS = [
    'content-type',
    'Authorization',
    'X-CSRFToken',
    'X-Requested-With',
]

ROOT_URLCONF = 'Food_Project.urls'

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

WSGI_APPLICATION = 'Food_Project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# REST_FRAMEWORK = {
#     'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
# }
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

DATABASES = {
    'default': dj_database_url.config(
        # Replace this value with your local database's connection string.
        default='postgresql://foodmanageproject_user:PXo55NdDebRacCOHTwJXaRFFUVpqRxXP@dpg-cr9v5grv2p9s73bg1v70-a.oregon-postgres.render.com/foodmanageproject',
    )
}

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'



# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env("EMAIL")
EMAIL_HOST_PASSWORD = env("EMAIL_PASSWORD")
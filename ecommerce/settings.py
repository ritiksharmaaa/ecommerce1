"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

#creditional 



import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Now you can access your environment variables using os.getenv

# please app you .env folder give creditial yor key id key secrst or mail app password 
RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID")
RAZORPAY_KEY_SECRET  = os.getenv("RAZORPAY_KEY_SECRET")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")

# Use the variables as needed in your script
# print(f" razorpay key id  {RAZORPAY_KEY_ID}")
# print(f"razorpay key secret : {RAZORPAY_KEY_SECRET}")
# print(f" email app password ;: {EMAIL_APP_PASSWORD}")



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR/'static'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&(yuq!3e!83&+e_ld!82lq+l&qtw*c=*apj1y$vmvx_9rj#ttw'

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
    #  'debug_toolbar',
    'app',
    'account',
]





MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',

]

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]



ROOT_URLCONF = 'ecommerce.urls'

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

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# settings.py

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR/'media'
# LOGIN_REDIRECT_URL = "/profile/" comment because we not redirect there we redirect 

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [STATIC_DIR,]

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# razorpay configure 


# JQUERY_VERSION = "3.3.1"


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ritik1832004@gmail.com'
EMAIL_HOST_PASSWORD = EMAIL_APP_PASSWORD
EMAIL_USE_TLS = True
# DEV Community — A constructive and inclusive social network for software developers. With you every step of your journey.



# views.py or wherever you want to send emails

# from django.core.mail import send_mail

# def send_email(request):
#     subject = 'Subject Here'
#     message = 'Here is the message.'
#     from_email = 'your@gmail.com'  # Replace with your Gmail email address
#     recipient_list = ['recipient@example.com']  # Replace with the recipient's email address

#     send_mail(subject, message, from_email, recipient_list)

#     # Add any additional logic or return statements as needed
"""
Django settings for guitarchords project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wx43gx&f4f=8)on7frpk_vm8!*_h5bwa(+%tbg8%+(-4%7_%bk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['pakumar.pythonanywhere.com', 'www.guitarclub.in']

#Admin When DEBUG=False and a view raises an exception, Django will email these people with the full exception information. Each member of the tuple should be a tuple of (Full name, email address)
ADMINS = (('Pawan','pawan.kumar.13.1991@gmail.com' ), ('Aditi','adiaggarwal89@gmail.com') , ('Pawan','Pawan.Kumar@mu-sigma.com') , ('Aditi','Aditi.Aggarwal@mu-sigma.com'))


#email
#EMAIL_BACKEND = ()


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
	'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'guitarchordsapp',
	#'djangodblog',
	'django.contrib.staticfiles',
'guitarchords',
    )

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/home/pakumar/GuitarClub/templates/'
    #'C:/Users/pakumar/python_practice/guitarchords/templates/',

    #'C:/Users/pakumar/python_practice/comparo/password_reset/templates/password_reset/'
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.gzip.GZipMiddleware',
	#'djangodblog.DBLogMiddleware',
)

ROOT_URLCONF = 'guitarchords.urls'

WSGI_APPLICATION = 'guitarchords.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'pakumar$dm_gc',
    'USER': 'pakumar',
    'PASSWORD': 'P@ssw0rd',
    'HOST':'mysql.server',
}
}


#DATABASES = {
#   'default': {
#      'ENGINE': 'django.db.backends.sqlite3',
#     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#}
#}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

MEDIA_ROOT = '/home/pakumar/GuitarClub/guitarchordsapp/static/'
MEDIA_URL = '/media/'


STATIC_URL = '/static/'
#STATIC_ROOT = '/home/pakumar/GuitarClub/guitarchordsapp/static/'

STATICFILES_DIRS = (
    '/home/pakumar/GuitarClub/guitarchordsapp/static/',
#'C:/Users/pakumar/python_practice/guitarchords/guitarchordsapp/static/',
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

import os
from django.core.exceptions import ImproperlyConfigured

"""
Django settings for sixstringapi project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', None)
if SECRET_KEY is None:
    raise ImproperlyConfigured('Please set the SECRET_KEY evironment variable')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DEBUG', False))

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*',]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = (
        'GET',
        'POST',
        'PUT',
        'PATCH',
        'DELETE',
        'OPTIONS'
    )


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'sixstring.utils.middleware.QueryCountDebugMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'sixstringapi.utils.middleware.DisableCSRF',
    'sixstringapi.utils.middleware.NoCacheAPI',
    'corsheaders.middleware.CorsMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sixstringapi.urls'

WSGI_APPLICATION = 'sixstringapi.wsgi.application'


PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)



# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {}
DATABASES['default'] =  dj_database_url.config()

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, '..', 'staticfiles')
STATIC_URL = '/static/'

MEDIA_ROOT =  os.path.join(BASE_DIR, '..', 'uploads')

STATICFILES_DIRS = (
    #os.path.join(BASE_DIR, 'static'),
)


EMAIL_BACKEND_TYPE = os.environ.get('EMAIL_BACKEND', 'CONSOLE')
if EMAIL_BACKEND_TYPE == 'POSTMARK':
    POSTMARK_API_KEY = os.environ.get('POSTMARK_API_KEY', False)
    POSTMARK_SENDER = os.environ.get('POSTMARK_SENDER', False)
    POSTMARK_TRACK_OPENS = True
    POSTMARK_TEST_MODE = False
    EMAIL_BACKEND = 'postmark.django_backend.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

import os
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's8*!*$hxsoqhf_&o$hyimr902aqvhled)&er#zd^h!o(ki4bb='
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


DATABASES = {
    'default': {
        'HOST': '127.0.0.1',
        'NAME': 'contact',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'postgres',
        'PASSWORD': 'coderslab',
    }
}

#DATABASES = {
#    'default': {
#        'HOST': '127.0.0.1',
#       'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'food',
#        'USER': 'postgres',
#        'PASSWORD': 'coderslab',
#    }
#}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static")
# ]

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_URL = '/login/'



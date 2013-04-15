import json
from settings import *

with open('/home/dotcloud/environment.json') as f:
      env = json.load(f)

try:
    from lakaxita.settings.secret_key import SECRET_KEY
except ImportError:
    from django.utils.crypto import get_random_string
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    SECRET_KEY = get_random_string(50, chars)
    with open(os.path.join(DIR, 'settings/secret_key.py'), 'w') as secret_key_file:
        secret_key_file.write("SECRET_KEY = '{}'".format(SECRET_KEY))


DEBUG = False
REQUIRE_DEBUG = DEBUG
TEMPLATE_DEBUG = DEBUG
SEND_BROKEN_LINK_EMAILS = DEBUG


ALLOWED_HOSTS = [
            'lakaxita-unaizalakain.dotcloud.com',
            'lakaxita.org',
            'www.lakaxita.org',
            ]

STATIC_ROOT = '/home/dotcloud/volatile/static/'
STATIC_URL = '/static/'
MEDIA_ROOT = '/home/dotcloud/data/media/'
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = os.path.join(STATIC_URL, 'grappelli')

CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': '/home/dotcloud/cache/',
            'TIMEOUT': 300,
            },
        }

CACHE_MIDDLEWARE_SECONDS = 300
MIDDLEWARE_CLASSES = ('django.middleware.cache.UpdateCacheMiddleware',
                    'django.middleware.gzip.GZipMiddleware',
                    'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware',
                    ) + \
                    MIDDLEWARE_CLASSES + \
                    ('django.middleware.http.ConditionalGetMiddleware',
                    'django.middleware.cache.FetchFromCacheMiddleware',
                    'django.middleware.clickjacking.XFrameOptionsMiddleware',
                    )

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
            },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'lakaxita',
            'USER': env['DOTCLOUD_DB_SQL_LOGIN'],
            'PASSWORD': env['DOTCLOUD_DB_SQL_PASSWORD'],
            'HOST': env['DOTCLOUD_DB_SQL_HOST'],
            'PORT': int(env['DOTCLOUD_DB_SQL_PORT']),
            }
        }


#ADMINS = (('Unai Zalakain', '{}@{}'.format('contact', 'unaizalakain.info')))
#MANAGERS = ADMINS

#EMAIL_SUBJECT_PREFIX = '[LAKAXITA]'
#EMAIL_HOST = ''
#EMAIL_HOST_USER = ''
#EMAIL_HOST_PASSWORD = ''
#DEFAULT_FROM_EMAIL = ''
#SERVER_EMAIL = ''

#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'


INSTALLED_APPS += ('raven.contrib.django.raven_compat',)
RAVEN_CONFIG = {
        'dsn': 'https://8be3d66e72604e20bb74712f39926d69:186dc82c9a4749129a9b9652cde82390@app.getsentry.com/4320',
        }

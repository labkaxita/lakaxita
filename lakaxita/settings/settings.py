import os


_ = lambda x: x
DIR = os.path.dirname(os.path.dirname(__file__))


SITE_ID = 1


USE_I18N = True
USE_L10N = True
TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'eu'
LANGUAGES = (
        ('eu', 'Euskara'),
        ('es', 'Castellano'),
        )
LOCALE_PATHS = ( os.path.join(DIR, 'locale'), )


MEDIA_ROOT = os.path.join(DIR, 'media')
FILEBROWSER_DIRECTORY = 'filebrowser'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(DIR, 'assets')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/grappelli/'
STATICFILES_DIRS = [os.path.join(DIR, 'static')]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
STATICFILES_STORAGE = 'require.storage.OptimizedCachedStaticFilesStorage'

SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

TEMPLATE_LOADERS = (
    'yammy.django_loaders.YammyFileSystemLoader',
    'yammy.django_loaders.YammyPackageLoader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_badbrowser.middleware.BrowserSupportDetection',
)

ROOT_URLCONF = 'lakaxita.urls'

TEMPLATE_DIRS = (
    os.path.join(DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'preferences.context_processors.preferences_cp',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.markup',
    'django.contrib.sitemaps',

    'south',
    'imagekit',
    'preferences',
    'django_badbrowser',
    'oembed',
    'markitup',
    'djcelery',
    'polymorphic',
    'mptt',
    'tastypie',
    'backbone_tastypie',
    'require',

    'grappelli.dashboard',
    'grappelli',
    'grappelli_modeltranslation',
    'modeltranslation',
    'filebrowser',
    'django.contrib.admin',

    'lakaxita',
    'lakaxita.news',
    'lakaxita.groups',
    'lakaxita.gallery',
    'lakaxita.lost_found',
    'lakaxita.attachments',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


JQUERY_URL = 'js/jquery.js'

MARKITUP_FILTER = ('markdown.markdown', {})
MARKITUP_SET = 'markitup/sets/markdown'
MARKITUP_SKIN = 'markitup/skins/markitup'
MARKITUP_AUTO_PREVIEW = True
OEMBED_DEFAULT_PARSE_HTML = False

GRAPPELLI_INDEX_DASHBOARD = 'lakaxita.dashboard.Dashboard'
GRAPPELLI_ADMIN_TITLE = 'lakaxita'

MODELTRANSLATION_TRANSLATION_FILES = ('lakaxita.translation',)

BADBROWSER_SUGGEST = ('firefox', 'chrome', 'safari', 'opera')
BADBROWSER_REQUIREMENTS = (
    ('firefox', '3.0'),
    ('chrome', '3.0'),
    ('microsoft internet explorer', '8'),
)

REQUIRE_BASE_URL = 'js'
REQUIRE_JS = 'lib/require.js'
REQUIRE_ENVIRONMENT = 'lakaxita.settings.require.NodeEnvironment'
REQUIRE_BUILD_PROFILE = 'main.build.js'
#REQUIRE_STANDALONE_MODULES = {'main': {
#    'out': 'main-built.js',
#    'build_profile': 'main.build.js',
#    }}

# add to WSGI too
import djcelery
djcelery.setup_loader()

BROKER_URL = 'django://'
CELERY_IMPORTS = ('lakaxita.lost_found.tasks',)
        
ATTACHMENTS = {
        'author_name': 'Irungo Lakaxita Gaztetxea',
        'author_url': 'https://lakaxita.org',
        }

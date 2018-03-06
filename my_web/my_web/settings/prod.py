from  my_web.settings.common import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_db',
        'HOST': 'db',
        'PORT': '3306',
        'USER': 'wim',
        'PASSWORD':'1800318',
    }
}

ALLOWED_HOSTS = ['spreader.online','www.spreader.online','127.0.0.1']



INSTALLED_APPS += [
    'django_logging',
]

MIDDLEWARE += [
    'django_logging.middleware.DjangoLoggingMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
]


DJANGO_LOGGING = {
    "CONSOLE_LOG": False
}
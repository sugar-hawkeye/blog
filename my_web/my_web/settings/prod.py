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

ALLOWED_HOSTS = ['spreader.online',]




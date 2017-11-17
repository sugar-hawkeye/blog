from  my_web.settings.common import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_db',
        'HOST': 'db',
        'PORT': '3309',
        'USER': 'wim',
        'PASSWORD':'1800318',
    }
}

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


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': { 
    'standard': {
    	'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'} 
    },
    'filters': {
        'require_debug_false': {
	    '()': 'django.utils.log.RequireDebugFalse',
	    }
	 },
     'handlers': {
          'null': {
	        'level': 'DEBUG',
		'class': 'logging.NullHandler',
	},
      'mail_admins': {
           'level': 'ERROR',
           'class': 'django.utils.log.AdminEmailHandler',
           'filters': ['require_debug_false'],
           'include_html': True,
	},
	'debug': {
	     'level':'DEBUG',
	     'class':'logging.handlers.RotatingFileHandler',
	     'filename': os.path.join(BASE_DIR, "log",'debug.log'),
	     'maxBytes':1024*1024*5,
	     'backupCount': 5,
	     'formatter':'standard',
	 },
	 'console':{
	      'level': 'DEBUG',
	      'class': 'logging.StreamHandler',
	      'formatter': 'standard',
	  },
    },
    'loggers': {
        'django': {
             'handlers': ['console'],
             'level': 'DEBUG',
             'propagate': False 
        },
        'django.request': {
                'handlers': ['debug','mail_admins'],
                'level': 'ERROR',
                'propagate': True,
        },
	
        'django.security.DisallowedHost': {
	        'handlers': ['null'],
                'propagate': False,
        },
   } 
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST= 'smtp.qq.com'
EMAIL_PORT= 25	
EMAIL_HOST_USER = '1402370971@qq.com' 
EMAIL_HOST_PASSWORD = 'tianyu1800318'
EMAIL_SUBJECT_PREFIX = 'django'
EMAIL_USE_TLS = True 
DEFAULT_FROM_EMAIL = SERVER_EMAIL = EMAIL_HOST_USER 

ADMINS = (
	('1402370971@qq.com',),
)


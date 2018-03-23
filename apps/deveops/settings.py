# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 09 13:49
# Author Yo
# Email YoLoveLife@outlook.com
"""
Django settings for devEops project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
from __future__ import absolute_import
import os
import django.db.backends.mysql
from deveops import conf as DEVEOPS_CONF
ENVIRONMENT=DEVEOPS_CONF.ENVIRONMENT

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1x$!#dwp2_6^tdgs1nv8pwgutbc#4m%#qaz!m!0h_f*%6fp+vt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'utils.apps.UtilsConfig',
    'authority.apps.AuthorityConfig',
    'validate.apps.ValidateConfig',
    'softlib.apps.SoftlibConfig',
    'manager.apps.ManagerConfig',
    'operation.apps.OperationConfig',
    'application.apps.MagicConfig',
    'execute.apps.ExecuteConfig',
    'concert.apps.ConcertConfig',
    'timeline.apps.TimelineConfig',
    'upload.apps.UploadConfig',
    'dns.apps.DnsConfig',
    'xmt.apps.XmtConfig',
    'rest_framework',
    'rest_framework_jwt',
    'corsheaders',
    'bootstrap3',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery', #celery
    'kombu.transport.django', #celery
    'channels',
]

#JWF
import datetime
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=1),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_SECRET_KEY': SECRET_KEY,
}


REST_FRAMEWORK = {
    # 'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE':10,
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.IsAdminUser'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
    )

}


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'deveops.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'deveops.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES={
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':DEVEOPS_CONF.DB_NAME,
        'USER':DEVEOPS_CONF.DB_USER,
        'PASSWORD':DEVEOPS_CONF.DB_PASSWD,
        'HOST':DEVEOPS_CONF.DB_HOST,
        'PORT':DEVEOPS_CONF.DB_PORT,
    },
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

# FILE_CHARSET='gb18030'
#
DEFAULT_CHARSET='utf-8'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# I18N translation
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale'), ]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_URL = '/static/'

# Upload files
UPLOAD_ROOT = PROJECT_DIR + '/upload'

# Media files
MEDIA_ROOT = PROJECT_DIR + '/media'
MEDIA_URL = '/media/'

#Work space
WORK_ROOT= PROJECT_DIR + '/workspace'

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, "static"),
    os.path.join(PROJECT_DIR, "media"),
    os.path.join(PROJECT_DIR, "workpsace"),
)

#LOGIN
LOGIN_URL='/validate/login'
AUTH_USER_MODEL='authority.ExtendUser'

#SESSION
SESSION_SAVE_EVERY_REQUEST=True
SESSION_EXPIRE_AT_BROWSER_CLOSE=True
SESSION_COOKIE_AGE=DEVEOPS_CONF.SESSION_COOKIE_AGE

#SSH
SSH_TIMEOUT=DEVEOPS_CONF.SSH_TIMEOUT

# LDAP
if ENVIRONMENT != 'TRAVIS':
    from django_auth_ldap.config import LDAPSearch,GroupOfNamesType
    import ldap
    AUTHENTICATION_BACKENDS = (
        'django_auth_ldap.backend.LDAPBackend',
        'django.contrib.auth.backends.ModelBackend',
    )
    AUTH_LDAP_SERVER_URI = "ldap://10.100.61.6:389"
    AUTH_LDAP_BIND_DN = "cn=tools,ou=Zabbix,ou=TEST,dc=zbjt,dc=com"
    AUTH_LDAP_BIND_PASSWORD = "7a$LIOOwxNO"

    OU = unicode('ou=集团所属公司,ou=浙报集团,dc=zbjt,dc=com','utf8')
    AUTH_LDAP_GROUP_SEARCH = LDAPSearch(OU,ldap.SCOPE_SUBTREE,"(objectClass=groupOfNames)")
    AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="cn")
    AUTH_LDAP_USER_SEARCH = LDAPSearch(OU,ldap.SCOPE_SUBTREE,"(&(objectClass=*)(sAMAccountName=%(user)s))")
    AUTH_LDAP_USER_ATTR_MAP = {
        "full_name": "cn",
        "description": "description",
        "first_name":"sn",
        "phone":"mobile",
    }
    AUTH_LDAP_ALWAYS_UPDATE_USER = True
    # AUTH_LDAP_MIRROR_GROUPS = True
else:
    pass


#Default devEops Env
PING_PLAYBOOK_TASK_ID=1

#RSA_KEY
RSA_KEY=DEVEOPS_CONF.RSA_KEY

#CHANNEL
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(DEVEOPS_CONF.REDIS_HOST,DEVEOPS_CONF.REDIS_PORT)],
        },
        "ROUTING": "deveops.routing.routing",
    },
}


# CELERY
import djcelery
djcelery.setup_loader()
# CELERY_BROKER_URL = 'redis://localhost:6379/0'
# BROKER_URL = 'redis://localhost:6379/0'
BROKER_URL = 'django://'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
# CELERY_RESULT_BACKEND = 'django://'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE


#FileUpload
# FILE_UPLOAD_HANDLERS=(
#     "django.core.files.uploadhandler.MemoryFileUploadHandler",
#     "django.core.files.uploadhandler.TemporaryFileUploadHandler"
# )
# import django.core.files.uploadhandler


#DJANGO LOG
# if DEBUG == True:
#     LOGGING_LEVEL = 'DEBUG'
# else:
#     LOGGING_LEVEL = 'WARNING'
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {
#        'standard': {
#            # 'format': '%(levelname)s-%(asctime)s-'
#            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'  #日志格式
#        }
#     },
#     'filters': {
#     },
#     'handlers': {
#         'default': {
#             'level':LOGGING_LEVEL,
#             'class':'logging.handlers.RotatingFileHandler',
#             'filename': 'logs/django.log',     #日志输出文件
#             'maxBytes': 1024*1024*5,                  #文件大小
#             'backupCount': 5,                         #备份份数
#             'formatter':'standard',                   #使用哪种formatters日志格式
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['default'],
#             'level': LOGGING_LEVEL,
#             'propagate': False
#         }
#     }
# }
#
# #PERSON LOG
# import logging
# import logging.config
# # logging.basicConfig(level=logging.DEBUG,
# #                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
# #                     datefmt='%a, %d %b %Y %H:%M:%S',
# #                     filename='logs/myapp.log',
# #                     filemode='w')
#
# logging.config.fileConfig('logging.ini')
# logger = logging.getLogger("deveops.api")
# logging.debug('This is debug message')
# logging.info('This is info message')
# logging.warning('This is warning message')
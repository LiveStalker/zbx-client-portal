from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': ZBXCP_DB_NAME,
        'USER': ZBXCP_DB_USER,
        'PASSWORD': ZBXCP_DB_PASSWD,
    }
}

ZBX_HOST = 'http://localhost:8080'
ZBX_USER = get_env_variable('ZBX_USER')
ZBX_PASSWD = get_env_variable('ZBX_PASSWD')
ZBX_GID = get_env_variable('ZBX_GID')

ZABBIX = {
    'HOST': ZBX_HOST,
    'USER': ZBX_USER,
    'PASSWD': ZBX_PASSWD,
    'DEFAULT_GID': ZBX_GID
}

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']

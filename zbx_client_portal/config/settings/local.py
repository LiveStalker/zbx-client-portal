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

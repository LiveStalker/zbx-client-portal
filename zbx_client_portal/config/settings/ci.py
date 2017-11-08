from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': ZBXCP_DB_NAME,
        'USER': ZBXCP_DB_USER,
        'PASSWORD': ZBXCP_DB_PASSWD,
    }
}

# we do not need zabbix config on ci server
ZABBIX = {
    'HOST': '',
    'USER': '',
    'PASSWD': ''
}

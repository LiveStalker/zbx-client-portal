from django.conf import settings
from pyzabbix import ZabbixAPI


class ZabbixGateway(object):
    def __init__(self):
        self.user = settings.ZABBIX['USER']
        self.passwd = settings.ZABBIX['PASSWD']
        self.zabbix = ZabbixAPI(settings.ZABBIX['HOST'])

    def get_version(self):
        return self.zabbix.api_version()

    def get_user(self, userid):
        self.zabbix.login(self.user, self.passwd)
        res = self.zabbix.user.get(userids=str(userid))
        self.zabbix.user.logout()
        if len(res) == 1:
            return res[0]['alias']
        else:
            return None

    def create_user(self, username, raw_password):
        """Create zabbix user.
        zabbix method: user.create
        zabbix doc: https://www.zabbix.com/documentation/3.4/manual/api/reference/user/create
        """
        self.zabbix.login(self.user, self.passwd)
        groups = [
            {'usrgrpid': str(settings.ZABBIX['DEFAULT_GID'])}
        ]
        # TODO catch exceptions
        res = self.zabbix.user.create(alias=username, passwd=raw_password, usrgrps=groups)
        self.zabbix.user.logout()
        return res['userids'][0]

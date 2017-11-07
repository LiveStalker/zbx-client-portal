from django.conf import settings
from pyzabbix import ZabbixAPI


class ZabbixGateway(object):
    def __init__(self):
        self.user = settings.ZABBIX['USER']
        self.passwd = settings.ZABBIX['PASSWD']
        self.zabbix = ZabbixAPI(settings.ZABBIX['HOST'])

    def get_version(self):
        return self.zabbix.api_version()

    def get_zabbix_user(self, userid):
        self.zabbix.login(self.user, self.passwd)
        params = {
            'userids': str(userid)
        }
        res = self.zabbix.user.get(userids=str(userid))
        self.zabbix.user.logout()
        if len(res) == 1:
            return res[0]['alias']
        else:
            return None

from .gateway import ZabbixGateway


def zabbix(request):
    client = ZabbixGateway()
    ctx = {
        'zabbix_version': client.get_version()
    }
    return ctx

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy as _l
from django.core.exceptions import ObjectDoesNotExist
from model_utils.models import TimeStampedModel

from zabbix.gateway import ZabbixGateway


class Project(TimeStampedModel):
    name = models.CharField(_('project name'), max_length=100, null=False, blank=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('owner'), related_name='owned_projects')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=_('members'),
                                     through='ProjectToMember', related_name='projects')
    zabbix_group_id = models.IntegerField(_('zabbix group id'), default=0)
    zabbix_gw = ZabbixGateway()

    class Meta:
        db_table = 'project'
        verbose_name = _l('project')
        verbose_name_plural = _l('projects')

    def __str__(self):
        try:
            return _('%s owned by %s') % (self.name, self.owner or None)
        except ObjectDoesNotExist:
            return _('%s orphaned or does not saved yet') % (self.name, )


class ProjectToMember(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('member'))
    project = models.ForeignKey('Project', verbose_name=_('project'))

    class Meta:
        db_table = 'project_member'
        verbose_name = _l('member')
        verbose_name_plural = _l('members')

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from model_utils.models import TimeStampedModel
from zabbix.gateway import ZabbixGateway


class UserProfile(TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    language = models.OneToOneField('UserLanguage')
    timezone = models.CharField(max_length=20, db_index=True, default=settings.TIME_ZONE)
    zabbix_user_id = models.IntegerField(default=0)

    class Meta:
        db_table = 'user_profile'
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

    def __str__(self):
        return ugettext('Profile: {}').format(self.user)

    def get_zabbix_version(self):
        client = ZabbixGateway()
        return client.get_version()

    def get_zabbix_user(self):
        client = ZabbixGateway()
        return client.get_user(self.zabbix_user_id)


class UserLanguage(models.Model):
    language = models.CharField(max_length=20, db_index=True)
    language_code = models.CharField(max_length=5, db_index=True)

    class Meta:
        db_table = 'language'
        ordering = ('language',)
        unique_together = (('language', 'language_code'),)
        verbose_name = _('language')
        verbose_name_plural = _('languages')

    def __str__(self):
        return ugettext(self.language)

from django.db import models, IntegrityError
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from model_utils.models import TimeStampedModel
from zabbix.gateway import ZabbixGateway


class UserProfile(TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    # TODO change CASCADE
    language = models.ForeignKey('UserLanguage', on_delete=models.CASCADE, null=True)
    timezone = models.CharField(max_length=20, db_index=True, default=settings.TIME_ZONE)
    zabbix_user_id = models.IntegerField(default=0)
    zabbix_gw = ZabbixGateway()

    class Meta:
        db_table = 'user_profile'
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

    def __str__(self):
        return ugettext('Profile: {}').format(self.user)

    def save(self, *args, **kwargs):
        if not self.pk:
            if 'username' not in kwargs or 'raw_password' not in kwargs:
                raise IntegrityError('Can not create zabbix user, missing username or password.')
            self.zabbix_user_id = self.create_zabbix_user(kwargs.pop('username'), kwargs.pop('raw_password'))
        super(UserProfile, self).save(*args, **kwargs)

    @staticmethod
    def get_default(language_code=settings.LANGUAGE_CODE):
        profile = UserProfile()
        # TODO catch if object does not exists
        language = UserLanguage.objects.get(language_code=language_code)
        profile.language = language
        return profile

    def get_zabbix_version(self):
        return self.zabbix_gw.get_version()

    def get_zabbix_user(self):
        return self.zabbix_gw.get_user(self.zabbix_user_id)

    def create_zabbix_user(self, username, raw_password):
        return self.zabbix_gw.create_user(username, raw_password)


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

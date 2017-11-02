from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _l
from django.utils.translation import ugettext as _


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    language = models.OneToOneField('UserLanguage')
    timezone = models.CharField(max_length=20, db_index=True, default=settings.TIME_ZONE)

    class Meta:
        db_table = 'user_profile'
        verbose_name = _l('User profile')
        verbose_name_plural = _l('User profiles')

    def __str__(self):
        return _('Profile: {}').format(self.user)


class UserLanguage(models.Model):
    language = models.CharField(max_length=20, db_index=True)
    language_code = models.CharField(max_length=5, db_index=True)

    class Meta:
        db_table = 'language'
        ordering = ('language',)
        unique_together = (('language', 'language_code'),)
        verbose_name = _l('Language')
        verbose_name_plural = _l('Languages')

    def __str__(self):
        return _(self.language)

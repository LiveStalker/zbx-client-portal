from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    language = models.OneToOneField('UserLanguage')
    timezone = models.CharField(max_length=20, db_index=True)

    class Meta:
        db_table = 'user_profile'
        verbose_name = _('User profile')
        verbose_name_plural = _('User profiles')

    def __str__(self):
        return 'Profile: {}'.format(self.user)


class UserLanguage(models.Model):
    language = models.CharField(max_length=20, db_index=True)

    class Meta:
        db_table = 'language'
        ordering = ('language',)
        verbose_name = _('Language')
        verbose_name_plural = _('Languages')

    def __str__(self):
        return self.language

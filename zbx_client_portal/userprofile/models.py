from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    language = models.CharField(max_length=20, db_index=True)
    timezone = models.CharField(max_length=20, db_index=True)

    class Meta:
        db_table = 'user_profile'
        verbose_name = _('User profile')
        verbose_name_plural = _('User profiles')

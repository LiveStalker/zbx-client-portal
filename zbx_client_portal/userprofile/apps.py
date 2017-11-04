from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class UserProfileConfig(AppConfig):
    name = 'userprofile'
    verbose_name = _('user profiles')

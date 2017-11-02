from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _l


class UserprofileConfig(AppConfig):
    name = 'userprofile'
    verbose_name = _l('User Profile')

import pytz
from django.forms import ModelForm, ChoiceField
from django.conf import settings
from .models import UserProfile


class TZChoiceField(ChoiceField):
    def __init__(self, required=True, widget=None, label=None, initial=None, help_text='', *args, **kwargs):
        timezones = pytz.common_timezones
        choices = zip(timezones, timezones)
        if not initial:
            initial = settings.TIME_ZONE
        super().__init__(choices, required, widget, label, initial, help_text, *args, **kwargs)


class UserProfileForm(ModelForm):
    timezone = TZChoiceField()

    class Meta:
        model = UserProfile
        fields = ('user', 'language', 'timezone')

import pytz
from django.middleware.locale import LocaleMiddleware as DjangoLocaleMiddleware
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.utils import timezone
from userprofile.models import UserProfile


class LocaleMiddleware(DjangoLocaleMiddleware):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(LocaleMiddleware, self).__init__(get_response)

    def process_request(self, request):
        self.load_user_conf(request)
        super(LocaleMiddleware, self).process_request(request)

    def process_response(self, request, response):
        return super(LocaleMiddleware, self).process_response(request, response)

    @staticmethod
    def load_user_conf(request):
        if not request.user.is_authenticated():
            return

        try:
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            return

        user_language = user_profile.language
        if user_language:
            request.session[LANGUAGE_SESSION_KEY] = user_language.language_code

        user_timezone = user_profile.timezone
        if user_timezone:
            request.timezone = pytz.timezone(user_timezone)
            timezone.activate(user_timezone)

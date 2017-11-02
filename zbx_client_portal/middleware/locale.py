import pytz
from django.middleware.locale import LocaleMiddleware as DjangoLocaleMiddleware
from django.utils.translation import LANGUAGE_SESSION_KEY
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

        language = user_profile.language
        if language:
            request.session[LANGUAGE_SESSION_KEY] = language.language_code

        timezone = user_profile.timezone
        if timezone:
            request.timezone = pytz.timezone(timezone)

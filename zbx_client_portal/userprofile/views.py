from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls.base import reverse
from django.views.decorators import cache
from django.utils.translation import ugettext as _


@cache.never_cache
def login(request):
    if request.user.is_authenticated:
        index_path = reverse('index')
        return HttpResponseRedirect(index_path)
    context = dict(
        title=_('Log in'),
        app_path=request.get_full_path(),
    )
    defaults = {
        'extra_context': context,
        'template_name': 'login.html',
    }
    return LoginView.as_view(**defaults)(request)


@cache.never_cache
def logout(request):
    return LogoutView.as_view()(request)

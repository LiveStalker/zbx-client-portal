from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate
from django.urls.base import reverse
from django.views.decorators import cache
from django.utils.translation import ugettext as _
from django.shortcuts import render, redirect
from .forms import SignUpForm


def account(request):
    if request.user.is_authenticated:
        return render(request, template_name='account.html')
    return redirect(reverse('userprofile:login'))


def signup(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                #login(request, user)
        else:
            form = SignUpForm()
        ctx = {
            'form': form,
            'app_path': request.get_full_path(),
        }
        return render(request, template_name='signup.html', context=ctx)
    return redirect(reverse('portal:index'))


@cache.never_cache
def login(request):
    if request.user.is_authenticated:
        index_path = reverse('index')
        return HttpResponseRedirect(index_path)
    ctx = dict(
        title=_('Log in'),
        app_path=request.get_full_path(),
    )
    defaults = {
        'extra_context': ctx,
        'template_name': 'login.html',
    }
    return LoginView.as_view(**defaults)(request)


@cache.never_cache
def logout(request):
    return LogoutView.as_view()(request)

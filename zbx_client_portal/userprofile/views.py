from django.db import transaction
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.utils.translation import ugettext as _
from django.views.decorators import cache

from .forms import SignUpForm
from .models import UserProfile


@login_required()
def account_view(request):
    return render(request, template_name='account.html')


def signup_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('portal:index'))
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                user = form.save()
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                profile = UserProfile.get_default()
                profile.user = user
                profile.save(username=username, raw_password=raw_password)
                login(request, user)
                return redirect(reverse('portal:index'))
    else:
        form = SignUpForm()
    ctx = {
        'form': form,
        'app_path': request.get_full_path(),
    }
    return render(request, template_name='signup.html', context=ctx)


@cache.never_cache
def login_view(request):
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
def logout_view(request):
    return LogoutView.as_view()(request)

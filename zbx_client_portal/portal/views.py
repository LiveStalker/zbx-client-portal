from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    if request.user.is_anonymous:
        return redirect(reverse('userprofile:login'))
    return render(request, 'index.html')

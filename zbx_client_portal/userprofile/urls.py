from django.conf.urls import url
from .views import login_view, logout_view, account_view, signup_view

urlpatterns = [
    url(r'^$', account_view, name='account'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^register/$', signup_view, name='signup'),
]

from django.conf.urls import url
from .views import login, logout, account, register
urlpatterns = [
    url(r'^$', account, name='account'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^register/$', register, name='register'),
]

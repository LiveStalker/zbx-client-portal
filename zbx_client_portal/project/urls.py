from django.conf.urls import url
from .views import ProjectCreate, ProjectUpdate, ProjectDelete, ProjectDetail

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', ProjectDetail.as_view(), name='detail'),
    url(r'^create/$', ProjectCreate.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/$', ProjectUpdate.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', ProjectDelete.as_view(), name='delete'),
]

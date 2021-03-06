from django.conf.urls import url, include
from .views import create_or_edit_task, delete_task

urlpatterns = [
    url(r'^(?P<project>\d+)/create/$', create_or_edit_task, name='create_task'),
    url(r'^(?P<pk>\d+)/project/(?P<project>\d+)/edit/$', create_or_edit_task, name='edit_task'),
    url(r'^(?P<pk>\d+)/delete/$', delete_task, name='delete_task'),
    ]

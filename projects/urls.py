from django.conf.urls import url, include
from .views import get_projects, project_info, create_or_edit_project, delete_project, view_only

urlpatterns = [
    url(r'^$', get_projects, name='get_projects'),
    url(r'^(?P<pk>\d+)/$', project_info, name='project_info'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_project, name='edit_project'),
    url(r'^create/$', create_or_edit_project, name="create_project"),
    url(r'^(?P<pk>\d+)/delete/$', delete_project, name='delete_project'),
    url(r'^(?P<pk>\d+)/view/$', view_only, name='view_only') 
    ]
from django.conf.urls import url
from .views import get_projects

urlpatterns = [
    url(r'^$', get_projects, name='get_projects')
    ]
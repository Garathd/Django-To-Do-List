from django.conf.urls import url, include
from django.contrib import admin
from . import urls_reset
from .views import register, profile, logout, login, edit_profile

handler500 = 'errors.views.page_error_found_custom'

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^edit_profile/$', edit_profile, name='edit_profile'),
    url(r'^password-reset/', include(urls_reset)),
]

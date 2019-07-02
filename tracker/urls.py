"""tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from projects import urls as urls_projects
from tasks import urls as urls_tasks
from dashboard.views import dashboard_view
from home.views import index
from .settings import MEDIA_ROOT
from django.views.static import serve

from products import urls as urls_products
from products.views import all_products
from cart import urls as urls_cart
from checkout import urls as urls_checkout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^dashboard/', dashboard_view, name='dashboard'),
    url(r'^projects/', include(urls_projects)),
    url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^tasks/', include(urls_tasks)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT }),
]

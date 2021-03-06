"""devices_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin

import article.views
import device_home.views
from device_query import views
from devices_management import settings
# modify
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^device-query/', include('device_query.urls')),
    url(r'^device-manage/', include('device_manage.urls')),
    url(r'^$', include('device_home.urls')),
    url(r'^accounts/', include('users.urls')),
    url(r'^profile/$', device_home.views.profile),
    url(r'^(?P<id>\d+)/$', article.views.detail, name='detail'),
]

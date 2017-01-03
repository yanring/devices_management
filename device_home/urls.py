from django.conf.urls import url

import article.views
from . import views

urlpatterns = [
    url(r'^$', article.views.home, name='home'),
]
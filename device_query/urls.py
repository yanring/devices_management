from django.conf.urls import url

from . import views
# modify
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^all-device$', views.all_device, name='index'),
    url(r'^check-repair$', views.check_repair, name='check_repair'),
    url(r'^check-lend$', views.check_lend, name='check_lend'),
    url(r'^check-discard$', views.check_discard, name='check_discard'),
    url(r'^state-check$', views.state_check, name='state_check'),
]
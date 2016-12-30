from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add-device$', views.add_device, name='add_device'),
    url(r'^add-repair$', views.add_repair, name='add_repair'),
    url(r'^add-lend', views.add_lend, name='add_lend'),
    url(r'^add-discard', views.add_discard, name='add_discard'),
    url(r'^state-manage$', views.state_manage, name='state_manage'),
    url(r'^state-manage/(?P<table>[a-zA-Z]+)(?P<id>\d+)/(?P<flag>\w+)$', views.lend_manage, name='lend_manage'),
]
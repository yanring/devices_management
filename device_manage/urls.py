from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add-device$', views.add_device, name='add_device'),
    url(r'^add-repair$', views.add_repair, name='add_repair'),
]
from django.shortcuts import render

from django.http import HttpResponse
from django_tables2 import tables

from device_home.models import Device


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def all_device(request):
    devices = BootStrapTable(Device.objects.all())
    return render(request, 'device_query/query_home2.html', locals())

class BootStrapTable(tables.Table):
    class Meta:
        model = Device
        attrs = {"class": "table table-hover table-striped"}
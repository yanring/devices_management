from django.shortcuts import render

from django.http import HttpResponse
from django_tables2 import tables

from device_home.models import Device, STATE_CHOICES, Repair, Lend, Discard


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def all_device(request):
    devices = BootStrapTable(Device.objects.all())
    return render(request, 'device_query/query_home2.html', locals())


def check_repair(request):
    devices = BootStrapTable(Device.objects.filter(state='repair'))
    return render(request, 'device_query/check_repair.html', locals())


def check_lend(request):
    devices = BootStrapTable(Device.objects.filter(state='lend'))
    return render(request, 'device_query/check_lend.html', locals())


def check_discard(request):
    devices = BootStrapTable(Device.objects.filter(state='discard'))
    return render(request, 'device_query/check_discard.html', locals())


def state_check(request):
    target_url = 'device_query/state_check.html'
    lend_request_list = Lend.objects.filter(finished="NO")
    repair_request_list = Repair.objects.filter(finished="NO")
    discard_request_list = Discard.objects.filter(finished="NO")
    return render(request, target_url, locals())


class BootStrapTable(tables.Table):
    class Meta:
        model = Device
        attrs = {"class": "table table-hover table-striped"}
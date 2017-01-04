# coding=utf-8
from django import forms

from django.shortcuts import render

from django.http import HttpResponse
from django_tables2 import tables

from device_home.models import Device, STATE_CHOICES, Repair, Lend, Discard, PRO_CHOICES


class SearchForm(forms.Form):
    Way = forms.ChoiceField(label='查询方式', choices=PRO_CHOICES, widget=forms.Select(
        attrs={'class': 'form-control', 'placeholder': "查询方式", 'style': 'width:30%'}))
    Word = forms.CharField(label='关键字', max_length=100, widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'form-control', 'placeholder': "关键字", 'style': 'width:30%'}))


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
    if request.method == 'POST':
        uf = SearchForm(request.POST)
        if uf.is_valid():
            way = uf.cleaned_data['Way']
            word = uf.cleaned_data['Word']
            if way == 'deviceId':
                devices = BootStrapTable(Device.objects.filter(deviceId=word, state='discard'))
            elif way == 'User':
                devices = BootStrapTable(Device.objects.filter(user=word, state='discard'))
            elif way == 'deviceName':
                devices = BootStrapTable(Device.objects.filter(deviceName=word, state='discard'))
            elif way == 'Department':
                devices = BootStrapTable(Device.objects.filter(department=word, state='discard'))
            else:
                print (way)
                devices = BootStrapTable(Device.objects.filter(state='discard'))
        else:
            devices = BootStrapTable(Device.objects.filter(state='discard'))
    else:
        uf = SearchForm()
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
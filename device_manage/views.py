# coding=utf-8
from django import forms
from django.shortcuts import render

from django.http import HttpResponse
from django_tables2 import tables

from device_home.models import Device, STATE_CHOICES


class UserFormRegist(forms.Form):
    User = forms.CharField(label='使用者姓名', max_length=100, widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'form-control', 'placeholder': "使用者姓名", 'style': 'width:60%'}))
    State = forms.ChoiceField(label='设备状态', choices=STATE_CHOICES, widget=forms.Select(
        attrs={'class': 'form-control', 'placeholder': "设备名称", 'style': 'width:60%'}))

    DeviceName = forms.CharField(label='设备名称', widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'form-control', 'placeholder': "设备名称", 'style': 'width:60%'}))
    Department = forms.CharField(label='所属部门', widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'form-control', 'placeholder': "部门", 'style': 'width:60% '}))


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def add_device(request):
    target_url = 'device_manage/add_device.html'
    if request.method == 'POST':
        uf = UserFormRegist(request.POST)
        login_flag = False
        # print(type(req))
        # print(req)
        if uf.is_valid():
            # 获得表单数据
            user = uf.cleaned_data['User']
            state = uf.cleaned_data['State']
            deviceName = uf.cleaned_data['DeviceName']
            department = uf.cleaned_data['Department']
            test = 'test'
            print(user)
            # 添加到数据库
            try:
                print(Device.objects.create(user=user, state=state, deviceName=deviceName, department=department))
                print("check")
                success = True
                print(test)
                test = 'test2'
                return render(request,target_url, locals())
            except Exception as e:
                login_flag = False
                error = True
                print(e)
                test = 'test'
                error_info = e
                return render(request,target_url,
                              {'uf': uf, 'error': error, 'error_info': error_info, 'test': test})



        else:
            return render(request,target_url, {'uf': uf})
    uf = UserFormRegist()
    return render(request, target_url, {'uf': uf})
def add_repair(request):
    target_url= 'device_manage/add_repair.html'
    if request.method == 'POST':
        uf = UserFormRegist(request.POST)
        login_flag = False
        # print(type(req))
        # print(req)
        if uf.is_valid():
            # 获得表单数据
            user = uf.cleaned_data['User']
            state = uf.cleaned_data['State']
            deviceName = uf.cleaned_data['DeviceName']
            department = uf.cleaned_data['Department']
            test = 'test'
            print(user)
            # 添加到数据库
            try:
                print(Device.objects.create(user=user, state=state, deviceName=deviceName, department=department))
                print("check")
                success = True
                print(test)
                test = 'test2'
                return render(request,target_url, locals())
            except Exception as e:
                login_flag = False
                error = True
                print(e)
                test = 'test'
                error_info = e
                return render(request,target_url,
                              {'uf': uf, 'error': error, 'error_info': error_info, 'test': test})



        else:
            return render(request,target_url, {'uf': uf})
    uf = UserFormRegist()
    return render(request, target_url, {'uf': uf})


class BootStrapTable(tables.Table):
    class Meta:
        model = Device
        attrs = {"class": "table table-hover table-striped"}

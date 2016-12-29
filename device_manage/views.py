# coding=utf-8
import time
from django import forms
from django.shortcuts import render

from django.http import HttpResponse
from django_tables2 import tables

from device_home.models import Device, STATE_CHOICES, Repair, Lend, Discard


class AddDeviceForm(forms.Form):
    User = forms.CharField(label='使用者姓名', max_length=100, widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'form-control', 'placeholder': "使用者姓名", 'style': 'width:60%'}))
    State = forms.ChoiceField(label='设备状态', choices=STATE_CHOICES, widget=forms.Select(
        attrs={'class': 'form-control', 'placeholder': "设备名称", 'style': 'width:60%'}))

    DeviceName = forms.CharField(label='设备名称', widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'form-control', 'placeholder': "设备名称", 'style': 'width:60%'}))
    Department = forms.CharField(label='所属部门', widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'form-control', 'placeholder': "部门", 'style': 'width:60% '}))


class AddRepairForm(forms.Form):
    DeviceId = forms.IntegerField(label='设备序号', min_value=0, widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'form-control', 'placeholder': "请填入正确的设备序号", 'style': 'width:60%'}))
    User = forms.CharField(label='使用者姓名', max_length=100, widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'form-control', 'placeholder': "使用者姓名", 'style': 'width:60%'}))
    Note = forms.CharField(label='备注', max_length=100, widget=forms.Textarea(
        attrs={'type': 'text', 'class': 'form-control', 'placeholder': "请填写设备损坏的详细信息", 'style': 'width:60%'}))


class AddLendForm(forms.Form):
    DeviceId = forms.IntegerField(label='设备序号', min_value=0, widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'form-control', 'placeholder': "请填入正确的设备序号", 'style': 'width:60%'}))
    User = forms.CharField(label='使用者姓名', max_length=100, widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'form-control', 'placeholder': "借用者姓名", 'style': 'width:60%'}))
    Note = forms.CharField(label='备注', max_length=100, widget=forms.Textarea(
        attrs={'type': 'text', 'class': 'form-control', 'placeholder': "请填写设备借用的备注", 'style': 'width:60%'}))
    # Finished = forms.CharField(label='所属部门', widget=forms.TextInput(
    #     attrs={'type': 'text', 'class': 'form-control', 'placeholder': "部门", 'style': 'width:60% '}))


class AddDiscardForm(forms.Form):
    DeviceId = forms.IntegerField(label='设备序号', min_value=0, widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'form-control', 'placeholder': "请填入正确的设备序号", 'style': 'width:60%'}))
    User = forms.CharField(label='使用者姓名', max_length=100, widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'form-control', 'placeholder': " 操作者姓名", 'style': 'width:60%'}))
    Note = forms.CharField(label='备注', max_length=100, widget=forms.Textarea(
        attrs={'type': 'text', 'class': 'form-control', 'placeholder': "请填写设备报废的原因", 'style': 'width:60%'}))
    # Finished = forms.CharField(label='所属部门', widget=forms.TextInput(
    #     attrs={'type': 'text', 'class': 'form-control', 'placeholder': "部门", 'style': 'width:60% '}))


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def add_device(request):
    target_url = 'device_manage/add_device.html'
    if request.method == 'POST':
        uf = AddDeviceForm(request.POST)
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
                return render(request, target_url, locals())
            except Exception as e:
                login_flag = False
                error = True
                print(e)
                test = 'test'
                error_info = e
                return render(request, target_url,
                              {'uf': uf, 'error': error, 'error_info': error_info, 'test': test})



        else:
            return render(request, target_url, {'uf': uf})
    uf = AddDeviceForm()
    return render(request, target_url, {'uf': uf})


def add_repair(request):
    target_url = 'device_manage/add_repair.html'
    if request.method == 'POST':
        uf = AddRepairForm(request.POST)
        login_flag = False
        # print(type(req))
        # print(req)
        if uf.is_valid():
            # 获得表单数据
            device_id = uf.cleaned_data['DeviceId']
            user = uf.cleaned_data['User']
            note = uf.cleaned_data['Note']
            # department = uf.cleaned_data['Department']
            test = 'test'
            date = date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # print(date)
            # device_instance = Device.objects.get(deviceId=device_id)
            # print(Repair.objects.create(deviceId=device_instance, user=user, note=note, finished='NO', date=date).__unicode__())

            # 添加到数据库
            try:
                device_instance = Device.objects.get(deviceId=device_id)
                print(Repair.objects.create(deviceId=device_instance, user=user, note=note, finished='NO',
                                            date=date).__unicode__())

                print("check")
                success = True
                print(test)
                test = 'test2'
                return render(request, target_url, locals())
            except Exception as e:
                login_flag = False
                error = True
                print(e)
                test = 'test'
                error_info = e
                return render(request, target_url,
                              {'uf': uf, 'error': error, 'error_info': error_info, 'test': test})



        else:
            return render(request, target_url, {'uf': uf})
    uf = AddRepairForm()
    return render(request, target_url, {'uf': uf})


def add_lend(request):
    target_url = 'device_manage/add_lend.html'
    if request.method == 'POST':
        uf = AddLendForm(request.POST)
        login_flag = False
        # print(type(req))
        # print(req)
        if uf.is_valid():
            # 获得表单数据
            device_id = uf.cleaned_data['DeviceId']
            user = uf.cleaned_data['User']
            note = uf.cleaned_data['Note']
            # department = uf.cleaned_data['Department']
            test = 'test'
            date = date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # print(date)
            # device_instance = Device.objects.get(deviceId=device_id)
            # print(Repair.objects.create(deviceId=device_instance, user=user, note=note, finished='NO', date=date).__unicode__())

            # 添加到数据库
            try:
                device_instance = Device.objects.get(deviceId=device_id)
                print(Lend.objects.create(deviceId=device_instance, user=user, note=note, finished='NO',
                                          date=date).__unicode__())

                print("check")
                success = True
                print(test)
                test = 'test2'
                return render(request, target_url, locals())
            except Exception as e:
                login_flag = False
                error = True
                print(e)
                test = 'test'
                error_info = e
                return render(request, target_url,
                              {'uf': uf, 'error': error, 'error_info': error_info, 'test': test})



        else:
            return render(request, target_url, {'uf': uf})
    uf = AddLendForm()
    return render(request, target_url, {'uf': uf})


def add_discard(request):
    target_url = 'device_manage/add_discard.html'
    if request.method == 'POST':
        uf = AddDiscardForm(request.POST)
        login_flag = False
        # print(type(req))
        # print(req)
        if uf.is_valid():
            # 获得表单数据
            device_id = uf.cleaned_data['DeviceId']
            user = uf.cleaned_data['User']
            note = uf.cleaned_data['Note']
            # department = uf.cleaned_data['Department']
            test = 'test'
            date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # print(date)
            # device_instance = Device.objects.get(deviceId=device_id)
            # print(Repair.objects.create(deviceId=device_instance, user=user, note=note, finished='NO', date=date).__unicode__())

            # 添加到数据库
            try:
                device_instance = Device.objects.get(deviceId=device_id)
                print(Discard.objects.create(deviceId=device_instance, user=user, note=note, finished='NO',
                                          date=date).__unicode__())

                print("check")
                success = True
                print(test)
                test = 'test2'
                return render(request, target_url, locals())
            except Exception as e:
                login_flag = False
                error = True
                print(e)
                test = 'test'
                error_info = e
                return render(request, target_url,
                              {'uf': uf, 'error': error, 'error_info': error_info, 'test': test})



        else:
            return render(request, target_url, {'uf': uf})
    uf = AddDiscardForm()
    return render(request, target_url, {'uf': uf})


class BootStrapTable(tables.Table):
    class Meta:
        model = Device
        attrs = {"class": "table table-hover table-striped"}

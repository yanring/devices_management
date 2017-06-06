# coding=utf-8
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    uid = models.AutoField(max_length=50, primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username

        # modify
# Create your models here.
class Device(models.Model):
    deviceId = models.AutoField(max_length=20, primary_key=True)
    user = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    deviceName = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    price = models.CharField(max_length=50,null=True)
    source_area = models.CharField(max_length=50,null=True)

    # python2使用__unicode__, python3使用__str__
    def __unicode__(self):
        return unicode(self.deviceId)


class Repair(models.Model):
    repairId = models.AutoField(max_length=20, primary_key=True)
    deviceId = models.ForeignKey(Device, related_name='+')
    user = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=50)
    finished = models.CharField(max_length=50)

    # python2使用__unicode__, python3使用__str__
    def __unicode__(self):
        return self.deviceId


class Lend(models.Model):
    lendId = models.AutoField(max_length=20, primary_key=True)
    deviceId = models.ForeignKey(Device, related_name='+')
    user = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=50)
    finished = models.CharField(max_length=50)
    return_time = models.DateTimeField(null=True)

    # python2使用__unicode__, python3使用__str__
    def __unicode__(self):
        return self.deviceId


class Discard(models.Model):
    discardId = models.AutoField(max_length=20, primary_key=True)
    deviceId = models.ForeignKey(Device, related_name='+')
    user = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=50)
    finished = models.CharField(max_length=50)

    # python2使用__unicode__, python3使用__str__
    def __unicode__(self):
        return self.deviceId

STATE_CHOICES = (
        ('normal', '正常'),
        ('lend', '借出'),
        ('discard', '报废'),
        ('repair', '维修中'),
)

PRO_CHOICES = (
        ('deviceId', '设备ID'),
        ('User', '使用者'),
        ('State', '状态'),
        ('deviceName', '设备名'),
        ('Department', '所属部门'),
)
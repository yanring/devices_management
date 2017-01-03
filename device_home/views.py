from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    home1 = {'home':"home"}
    return render(request,'device_home/home.html',locals())
def profile(request):
    pass
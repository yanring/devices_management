from django.contrib import admin

# Register your models here.
from device_home.models import Discard,Device,Repair,Lend,User

admin.site.register(Device)
admin.site.register(Repair)
admin.site.register(Discard)
admin.site.register(Lend)
admin.site.register(User)
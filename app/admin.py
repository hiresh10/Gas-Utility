from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(UserMaster)
class UserMasterAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'password')

@admin.register(ServiceRequest)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'usermasterid', 'username', 'request_type','request_detail', 'request_file', 'request_time', 'request_date', 'request_status', 'resolution_date')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'contact')
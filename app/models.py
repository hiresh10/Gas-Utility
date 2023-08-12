from django.db import models

# Create your models here.
class UserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

class Customer(models.Model):
    custermer_id = models.ForeignKey('UserMaster', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.BigIntegerField()

    

class ServiceRequest(models.Model):
    usermasterid = models.ForeignKey('UserMaster', on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    request_type = models.CharField(max_length=100)
    request_detail = models.CharField(max_length=500)
    request_file = models.ImageField(upload_to='app/request_file')
    request_time = models.TimeField(auto_now=True)
    request_date = models.DateField(auto_now=True)
    request_status = models.BooleanField(default=False)
    resolution_date = models.DateField(blank=True, null=True)
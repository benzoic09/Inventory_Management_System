from django.db import models
from django.utils import timezone

# Create your models here.
class devicetype(models.Model):
    model = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Inactive')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.model
    
class Devices(models.Model):
    MacAddress=models.CharField(max_length=50,blank=True, null=True)
    SerialNo=models.CharField(max_length=50,blank=True, null=True) #this can be blank
    MobileNo = models.CharField(max_length=10,blank=False, null=False)
    Model = models.ForeignKey(devicetype, on_delete=models.PROTECT)
    Cover = models.BooleanField(default=False)
    status = models.CharField(max_length=1, choices=(('A','Active'),('D','Damaged'),('D','Dead')), default='A')
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.MacAddress


class branch(models.Model):
    branch= models.CharField(max_length=30)

    def __str__(self):
        return self.branch  


class employees(models.Model):
    empno = models.CharField(max_length=30)
    Name = models.CharField(max_length=250)
    Department = models.CharField(max_length=250)
    branch = models.ForeignKey(branch, on_delete=models.PROTECT)
    BusinessUnit = models.CharField(max_length=2, choices=(('1','sales'),('2','Delivery'),('3','Warehouse')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.empno




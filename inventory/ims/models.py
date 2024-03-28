from django.db import models
from django.utils import timezone

# Create your models here.
class devicetype(models.Model):
    model = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=(('Active','Active'),('Inactive','Inactive')), default=1)
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
    status = models.CharField(max_length=10, choices=(('Active','Active'),('Damaged','Damaged'),('Dead','Dead')), default='A')
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.MacAddress


class employees(models.Model):
    empno = models.CharField(max_length=30)
    Name = models.CharField(max_length=250)
    branch = models.CharField(max_length=3, choices=(('NBI','NAIRONI'),('KSM','KISUMU'),('MSA','MOMBASA')))
    Department = models.CharField(max_length=20, choices=(('sales', 'Sales'),('delivery', 'Delivery'),('warehouse', 'Warehouse')))
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.empno




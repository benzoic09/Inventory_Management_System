from django.db import models
from django.utils import timezone

# Create your models here.
class devicetype(models.Model):
    model = models.CharField(max_length=250)
    type = models.TextField()
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Inactive')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.model
    
class devices(models.Model):
    MacAddress=models.CharField(max_length=100,blank=True, null=True)
    SerialNo=models.CharField(max_length=250,blank=True, null=True) #this can be blank
    MobileNo = models.TextField()
    Model = models.ForeignKey(devicetype, on_delete=models.PROTECT)
    ScreenProtector = models.BooleanField(default=False)
    Cover = models.BooleanField(default=False)
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Damaged'),('3','Dead')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.MacAddress + ' - ' + self.Model # to reseaech more on this 


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




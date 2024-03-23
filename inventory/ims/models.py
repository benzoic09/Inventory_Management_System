from django.db import models

# Create your models here.
class devicetype(models.Model):
    model = models.CharField(max_length=250)
    type = models.TextField()
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Inactive')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Devices(models.Model):
    MacAddress=models.CharField(max_length=100,blank=True, null=True)
    SerialNo=models.CharField(max_length=250,blank=True, null=True) #this can be blank
    MobileNo = models.TextField()
    Model = models.ForeignKey(devicetype)
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Damaged'),('3','Dead')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.MacAddress + ' - ' + self.name # to reseaech more on this 
    
    

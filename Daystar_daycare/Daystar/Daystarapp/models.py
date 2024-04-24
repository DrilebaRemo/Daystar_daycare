from django.db import models
from django.utils import timezone

# Create your models here.
class AdminReg(models.Model):
    adminemail = models.CharField(max_length=100, null=True, blank=True)
    adminpassw = models.CharField(max_length=100, null=True, blank=True)
    adminname = models.CharField(max_length=100, null=True, blank=True)
    adminphone = models.IntegerField( null=True, blank=True)

    def __str__(self):
        return self.adminname
    
class Adminlogin(models.Model):
    adminpassw = models.CharField(max_length=100, null=True, blank=True)
    adminname = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.adminname
    
class Babiesreg(models.Model):
    babyname = models.CharField(max_length=100, null=True, blank=True)
    babyage = models.IntegerField(null=True, blank=True, default=0)
    babygender = models.CharField(max_length=100, null=True, blank=True)
    babyloc = models.CharField(max_length=100, null=True, blank=True)
    babyparent = models.CharField(max_length=100, null=True, blank=True)
    babyno = models.IntegerField(max_length=100, null=True, blank=True)
    babypay = models.CharField(max_length=10, default="UGX", null=True, blank=True)


    def __str__(self):
        return self.babyname

class Sitterreg(models.Model):
    sittername = models.CharField(max_length=100, null=True, blank=True)
    siiterbirth = models.DateTimeField( null=True, blank=True)
    sittergender = models.CharField(max_length=100, null=True, blank=True)
    sitterloc = models.CharField(max_length=100, null=True, blank=True)
    sitterNIN = models.IntegerField(max_length=100, null=True, blank=True)
    sitterno = models.IntegerField(max_length=100, null=True, blank=True)
    sitterkin =models.CharField(max_length=100, null=True, blank=True)
    sitterreco = models.CharField(max_length=100, null=True, blank=True)
    sitterreligion = models.CharField(max_length=100, null=True, blank=True)
    sittereduc = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.sittername
    




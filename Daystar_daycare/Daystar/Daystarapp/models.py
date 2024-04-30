from django.db import models
from django.utils import timezone

# Create your models here.
class AdminReg(models.Model):
    adminemail = models.CharField(max_length=100, null=True, blank=True)
    adminname = models.CharField(max_length=100, null=True, blank=True, unique=True)
    adminphone = models.IntegerField( null=True, blank=True)

    USERNAME_FIELD = 'adminname'
    def __str__(self):
        return f"{self.adminname} - {self.adminpassw}"
    
class Adminlogin(models.Model):
    login = models.ForeignKey(AdminReg, on_delete=models.SET_NULL, null=True, blank=True)
    adminpassw = models.CharField(max_length=100, null=True, blank=True)
    adminnamee = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.adminnamee
    
class Babiesreg(models.Model):
    babyname = models.CharField(max_length=100, null=True, blank=True)
    babyage = models.IntegerField(null=True, blank=True, default=0)
    babygender = models.CharField(max_length=100, null=True, blank=True)
    babyloc = models.CharField(max_length=100, null=True, blank=True)
    babyparent = models.CharField(max_length=100, null=True, blank=True)
    babyno = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.babyname} - {self.babyno}"

class Sitterreg(models.Model):
    sittername = models.CharField(max_length=100, null=True, blank=True)
    sitterbirth = models.DateField( null=True, blank=True)
    sittergender = models.CharField(max_length=100, null=True, blank=True)
    sitterloc = models.CharField(max_length=100, null=True, blank=True)
    sitterNIN = models.CharField( max_length=30, null=True, blank=True)
    sitterno = models.IntegerField( null=True, blank=True)
    sitterkin =models.CharField(max_length=100, null=True, blank=True)
    sitterreco = models.CharField(max_length=100, null=True, blank=True)
    sitterreligion = models.CharField(max_length=100, null=True, blank=True)
    sittereduc = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.sittername} - {self.sitterno}"
    
class Timein(models.Model):
    babydrop = models.ForeignKey(Babiesreg, on_delete=models.CASCADE)
    picker = models.CharField(max_length=100, null=True, blank=True)
    timein = models.DateTimeField(null=True, blank=True)
    babypay = models.CharField(max_length=10, default="UGX", null=True, blank=True)
    periodstay = models.CharField(max_length=10,null=True, blank=True)

    def __str__(self):
        return f"{self.babydrop.babyname} - {self.periodstay}"

class Timeout(models.Model):
    babypick = models.ForeignKey(Timein, on_delete=models.CASCADE)
    timeout = models.DateTimeField(blank=True, null=True)
    dropper = models.CharField(max_length=100, null=True, blank=True)
    comment = models.CharField(max_length=200, blank=True, null=True)

class Inventory(models.Model):
    milk = models.IntegerField( null=True, blank=True)
    diapers = models.IntegerField( null=True, blank=True)
    dolls= models.IntegerField(null=True, blank=True)
    fruits= models.IntegerField(null=True, blank=True)

class Teachpayer(models.Model):
    tcontact = models.IntegerField(null=True, blank=True)
    taccnum = models.IntegerField(null=True, blank=True)
    tamount = models.IntegerField(null=True, blank=True)


class Sales(models.Model):
    amount = models.IntegerField(null=True, blank=True)




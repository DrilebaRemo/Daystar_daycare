from django.db import models
from django.utils import timezone

# Create your models here.
class AdminReg(models.Model):
    adminemail = models.CharField(max_length=100, null=True, blank=True)
    adminname = models.CharField(max_length=100, null=True, blank=True, unique=True)
    adminphone = models.IntegerField( null=True, blank=True)

    USERNAME_FIELD = 'adminname'
    def __str__(self):
        return {self.adminname}
    
class Adminlogin(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    

    def __str__(self):
        return self.adminnamee
    
class Babiesreg(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    STAY_CHOICES = [
        ('fullday', 'Full day'),
        ('halfday', 'Half day'),
        ('monthly', 'Monthly'),
    ]
    babyname = models.CharField(max_length=100, null=True, blank=True)
    babyage = models.IntegerField(null=True, blank=True)
    baby_gender = models.CharField(max_length=100, null=True, blank=True, choices= GENDER_CHOICES) 
    babyloc = models.CharField(max_length=100, null=True, blank=True)
    babyparent = models.CharField(max_length=100, null=True, blank=True)
    babyno = models.IntegerField(null=True, blank=True)
    dropper = models.CharField(max_length=100, null=True, blank=True)
    timein = models.DateTimeField(null=True, blank=True)
    period_of_stay = models.CharField(max_length=10,null=True, blank=True, choices=STAY_CHOICES)
    babypay = models.IntegerField( null=True, blank=True)
    
    def __str__(self):
        return self.babyname

class Sitterreg(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    sittername = models.CharField(max_length=100, null=True, blank=True)
    sitterbirth = models.DateField( null=True, blank=True)
    sitter_gender = models.CharField(max_length=100, null=True, blank=True, choices=GENDER_CHOICES)
    sitterloc = models.CharField(max_length=100, null=True, blank=True)
    sitterNIN = models.CharField( max_length=30, null=True, blank=True)
    sitterno = models.IntegerField( null=True, blank=True)
    sitterkin =models.CharField(max_length=100, null=True, blank=True)
    sitterreco = models.CharField(max_length=100, null=True, blank=True)
    sitterreligion = models.CharField(max_length=100, null=True, blank=True)
    sittereduc = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.sittername
    

class Timeout(models.Model):
    baby_being_picked = models.ForeignKey(Babiesreg, on_delete=models.CASCADE)
    timeout = models.DateTimeField(blank=True, null=True)
    dropper = models.CharField(max_length=100, null=True, blank=True)
    comment = models.CharField(max_length=200, blank=True, null=True)

class Procure(models.Model):
    pitems = models.CharField( max_length= 100, null=True, blank=True)
    amount = models.IntegerField( blank=True, null=True)
    def __str__(self):
        return self.pitems
    
class Dollstall(models.Model):
    dolls = models.CharField(max_length=50, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    unitprice = models.IntegerField(null = True, blank=True)
    def __str__(self):
        return self.dolls
    


class Sales(models.Model):
    item = models.ForeignKey(Dollstall, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    sell_to = models.ForeignKey(Babiesreg, on_delete=models.CASCADE)
    price = models.IntegerField(null=True, blank=True)
    datesale = models.DateTimeField(null=True, blank=True)
    


class Assignbaby(models.Model):
    baby_being_assigned_to =models.ForeignKey(Babiesreg, on_delete=models.CASCADE)
    sitter_name = models.ForeignKey(Sitterreg, on_delete=models.CASCADE)
    attendance = models.CharField(max_length=10, blank=True, null=True)
    daypay = models.IntegerField(null=True, blank=True)
   

class Procuregive(models.Model):
    procurement_item = models.ForeignKey(Procure, on_delete=models.CASCADE)
    procurequantity = models.IntegerField(null=True, blank=True)
    baby_being_given_to = models.ForeignKey(Babiesreg, on_delete=models.CASCADE)



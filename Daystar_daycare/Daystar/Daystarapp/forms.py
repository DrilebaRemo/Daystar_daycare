from django.forms import ModelForm
from .models import *
 # Create your models here.
class AddbabyForm(ModelForm):
    class Meta:
        model = Babiesreg
        fields = '__all__'

class AdminregForm(ModelForm):
    class Meta:
        model = AdminReg
        fields = '__all__'

class AdminloginForm(ModelForm):
    class Meta:
        model = Adminlogin
        fields = '__all__'

class AddsitterForm(ModelForm):
    class Meta:
        model = Sitterreg
        fields = '__all__'
from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

 # Create your models here.
class AddbabyForm(forms.ModelForm):
    class Meta:
        model = Babiesreg
        fields = '__all__'
        labels = {
            'babyname': False,
            'babyage': False,
            'babygender': False,
            'babyloc': False,
            'babyparent': False,
            'babyno': False,
        }    
        widgets = {
            'babyname': forms.TextInput(attrs={'placeholder': 'Your name...'}),
            'babyage': forms.NumberInput(attrs={'placeholder': 'Your age...'}),
            'babygender': forms.TextInput(attrs={'placeholder': 'Your gender...'}),
            'babyloc': forms.TextInput(attrs={'placeholder': 'Your location...'}),
            'babyparent': forms.TextInput(attrs={'placeholder': 'Your parent...'}),
            'babyno': forms.NumberInput(attrs={'placeholder': 'Your phone number...'}),
        }

class AdminRegForm(UserCreationForm):
    class Meta:
        model = AdminReg
        fields = '__all__'
        labels = {
            'adminemail': False,
            'adminname': False,
            'adminphone': False,
        }
        widgets = {
    'adminemail': forms.EmailInput(attrs={'placeholder': 'Your email...'}),
    'adminname': forms.TextInput(attrs={'placeholder': 'Your name...'}),
    'adminphone': forms.NumberInput(attrs={'placeholder': 'Your phone number...'}),
        }


class AdminloginForm(ModelForm):
    class Meta:
        model = Adminlogin
        fields = '__all__'
        labels = {
            'adminpassw': False,
            'adminnamee': False,
        }
        widgets = {
        'adminpassw': forms.PasswordInput(attrs={'placeholder': 'Your password...'}),
        'adminnamee': forms.TextInput(attrs={'placeholder': 'Your name...'}),
        }

class AddsitterForm(ModelForm):
    class Meta:
        model = Sitterreg
        fields = '__all__'
        labels = {
           'sittername': False,
           'sitterbirth': False,
           'sittergender': False,
           'sitterloc': False,
           'sitterNIN': False,
           'sitterno': False,
           'sitterkin': False,
           'sitterreco': False,
           'sitterreligion': False,
           'sittereduc': False,
        }
        widgets = {
           'sittername': forms.TextInput(attrs={'placeholder': 'Your name...'}),
           'sitterbirth': forms.DateInput(attrs={'placeholder': 'Your birth date...'}),
           'sittergender': forms.TextInput(attrs={'placeholder': 'Your gender...'}),
           'sitterloc': forms.TextInput(attrs={'placeholder': 'Your location...'}),
           'sitterNIN': forms.TextInput(attrs={'placeholder': 'Your NIN...'}),
           'sitterno': forms.NumberInput(attrs={'placeholder': 'Your sitter number...'}),
           'sitterkin': forms.TextInput(attrs={'placeholder': 'Your kins name...'}),
           'sitterreco': forms.TextInput(attrs={'placeholder': 'Your recommendation name...'}),
           'sitterreligion': forms.TextInput(attrs={'placeholder': 'Your religion...'}),
           'sittereduc': forms.TextInput(attrs={'placeholder': 'Your level of education...'}),
        }

class PaysForm(ModelForm):
    class Meta:
        model = Teachpayer
        fields = '__all__'
        labels = {
            'tname': False,
            'taccnum': False,
            'tcontact': False,
            'tamount': False,
        }
        widgets = {
            'tname': forms.TextInput(attrs={'placeholder': 'form-control'}),
            'taccnum': forms.NumberInput(attrs={'placeholder': 'form-control'}),
            'tcontact': forms.NumberInput(attrs={'placeholder': 'form-control'}),
            'tamount': forms.NumberInput(attrs={'placeholder': 'form-control'}),
        }

class DropbabyForm(ModelForm):
    class Meta:
        model = Timein
        fields = '__all__'
        labels = {
           'picker': False,
           'timein': False,
           'babypay': False,
           'periodstay': False,
        }
        widgets = {
           'picker': forms.TextInput(attrs={'placeholder': 'Picker name...'}),
           'timein': forms.DateTimeInput(attrs={'placeholder': 'Time...'}),
           'periodstay': forms.TextInput(attrs={'placeholder': 'Period of stay...'}),
           'babypay': forms.NumberInput(attrs={'placeholder': 'UGX...'}),
        }
   
class PickbabyForm(ModelForm):
    class Meta:
        model = Timeout
        fields = '__all__'
        labels = {
           'dropper': False,
           'timeout': False,
           'comment': False,
        }
        widgets = {
            'dropper': forms.TextInput(attrs={'placeholder': 'Dropper name...'}),
            'timeout': forms.DateTimeInput(attrs={'placeholder': 'Time picked...'}),
            'comment': forms.TextInput(attrs={'placeholder': 'Comment...'}),
        }
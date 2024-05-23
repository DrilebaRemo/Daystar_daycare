from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

 # Create your models here.
class AddbabyForm(forms.ModelForm):
    class Meta:
        model = Babiesreg
        fields = '__all__'
        labels = {
            'babyname': False,
            'babyage': False,
            #'babygender': False,
            'babyloc': False,
            'babyparent': False,
            'babyno': False,
            'dropper': False,
            'timein': False,
            #'periodstay': False,
            'babypay': False,

        }   
        widgets = {
            'babyname': forms.TextInput(attrs={'placeholder': 'Baby name...', 'required':'required'}),
            'babyage': forms.NumberInput(attrs={'placeholder': 'Baby age...', 'required':'required'}),
            'babygender': forms.Select(attrs={'placeholder': 'Your gender...', 'required': 'required'}),
            'babyloc': forms.TextInput(attrs={'placeholder': 'Baby location...', 'required':'required'}),
            'babyparent': forms.TextInput(attrs={'placeholder': 'Parent name...', 'required':'required'}),
            'babyno': forms.NumberInput(attrs={'placeholder': 'Baby number...', 'required':'required'}),
            'dropper': forms.TextInput(attrs={'placeholder': 'Dropper name...', 'required':'required'}),
            'timein': forms.DateTimeInput(attrs={'placeholder': 'Time in...', 'required':'required'}),
            'periodstay': forms.Select(attrs={'placeholder': 'Your period stay...','required':'required' }),
            'babypay': forms.NumberInput(attrs={'placeholder': 'Pay...', 'required':'required'}),
        }


class AdminRegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            #'username': False,
            #'email': False,
            #'password1': False,
            #'password2': False,
        
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Your name...', 'required':'required'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email...', 'required':'required'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Your password...', 'required':'required'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Your password...', 'required':'required'}),
        }


class AdminloginForm(ModelForm):
    class Meta:
        model = Adminlogin
        fields = '__all__'
        labels = {
            'username': False,
            'password': False,
        }
        widgets = {
        'username': forms.TextInput(attrs={'placeholder': 'Your name...', 'required':'required'}),
        'password': forms.PasswordInput(attrs={'placeholder': 'Your password...', 'required':'required'}),
        }

class AddsitterForm(ModelForm):
    class Meta:
        model = Sitterreg
        fields = '__all__'
        labels = {
           'sittername': False,
           'sitterbirth': False,
           #'sitter_gender': False,
           'sitterloc': False,
           'sitterNIN': False,
           'sitterno': False,
           'sitterkin': False,
           'sitterreco': False,
           'sitterreligion': False,
           'sittereduc': False,
        }
        widgets = {
           'sittername': forms.TextInput(attrs={'placeholder': 'Your name...', 'required':'required'}),
           'sitterbirth': forms.DateInput(attrs={'placeholder': 'Your birth date...', 'required':'required'}),
           'sitter_gender': forms.Select(attrs={'placeholder': 'Your gender...', 'required':'required', 'class': 'mykeys'}),
           'sitterloc': forms.TextInput(attrs={'placeholder': 'Your location...', 'required':'required'}),
           'sitterNIN': forms.TextInput(attrs={'placeholder': 'Your NIN...', 'required':'required'}),
           'sitterno': forms.NumberInput(attrs={'placeholder': 'Your sitter number...', 'required':'required'}),
           'sitterkin': forms.TextInput(attrs={'placeholder': 'Your kins name...', 'required':'required'}),
           'sitterreco': forms.TextInput(attrs={'placeholder': 'Your reference name...', 'required':'required'}),
           'sitterreligion': forms.TextInput(attrs={'placeholder': 'Your religion...'}),
           'sittereduc': forms.TextInput(attrs={'placeholder': 'Your level of education...', 'required':'required'}),
        }

class AssignbabyForm(ModelForm):
    class Meta:
        model = Assignbaby
        fields = '__all__'
        labels = {
            #'baby_being_assigned_to': False,
            #'sitter_name': False,
            'attendance': False,
            'daypay': False,
        }
        widgets = {
            'baby_being_assigned_to': forms.Select(attrs={'placeholder': 'Assign baby...', 'required':'required'}),
            'sitter_name': forms.Select(attrs={'placeholder': 'Name of sitter...', 'required':'required'}),
            'attendance': forms.TextInput(attrs={'placeholder': 'Sitters attendance...', 'required':'required'}),
            'daypay': forms.NumberInput(attrs={'placeholder': 'Payment...', 'required':'required'}),
        }
   
class PickbabyForm(ModelForm):
    class Meta:
        model = Timeout
        fields = '__all__'
        labels = {
           #'baby_being_picked': False,
           'timeout': False,
           'dropper': False,
           'comment': False,
        }
        widgets = {
           'baby_being_picked': forms.Select(attrs={'placeholder': 'Baby name...', 'class': 'mykeys'}),
            'timeout': forms.DateTimeInput(attrs={'placeholder': 'Time picked...', 'required':'required'}),
            'dropper': forms.TextInput(attrs={'placeholder': 'Picker name...', 'required':'required'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Comment...', 'class': 'textarea'}),
        }


class DollRegForm(ModelForm):
    class Meta:
        model = Dollstall
        fields = '__all__'
        labels = {
            'dolls': False,
            'quantity': False,
            'unitprice': False,
        }
        widgets = {
            'dolls': forms.TextInput(attrs={'placeholder': 'Dolls...', 'required':'required'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Quantity...', 'required':'required'}),
            'unitprice': forms.NumberInput(attrs={'placeholder': 'Unit price UGX...', 'required':'required'}),
        }


class SalesForm(ModelForm):
    class Meta:
        model = Sales
        fields =['doll_item', 'quantity', 'sell_to_baby','datesale', 'total_price']
        labels = {
            'quantity': False,
            'datesale': False,
            'total_price': False,
        }
        widgets = {
          'doll_item': forms.Select(attrs={'placeholder': 'Doll/Toy...', 'required':'required'}),
           'quantity': forms.NumberInput(attrs={'placeholder': 'Quantity...', 'required':'required'}),
           'sell_to_baby': forms.Select(attrs={'placeholder': 'Sell to baby...', 'required':'required'}),
           'total_price': forms.NumberInput(attrs={'placeholder': 'Total price...', 'required':'required'}),
           'datesale': forms.DateTimeInput(attrs={'placeholder': 'Date of sale...', 'required':'required'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        doll_item = cleaned_data.get('doll_item')
        quantity = cleaned_data.get('quantity')

        if doll_item and quantity:
            if doll_item.quantity <= 0:
                raise forms.ValidationError(f"OUT OF STOCK")
            if doll_item.quantity < quantity:
                raise forms.ValidationError(f"NOT ENOUGH")
        return cleaned_data

class ProcurementForm(ModelForm):
    class Meta:
        model = Procure
        fields = '__all__'
        labels = {
            'pitems': False,
            'amount': False,
        }
        widgets = {
            'pitems': forms.TextInput(attrs={'placeholder': 'Item...', 'required':'required'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'Amount...', 'required':'required'}),
        }

class ProcurementgiveForm(ModelForm):
    class Meta:
        model = Procuregive
        fields = '__all__'
        labels = {
            #'procurement_item': False,
            #'baby_being_given_to': False,
            'amount': False,
        }
        widgets = {
            'procurement_item': forms.Select(attrs={'placeholder': 'Item...', 'required': 'required'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'Amount...', 'required':'required'}),
            'baby_being_given_to': forms.Select(attrs={'placeholder': 'Baby name...', 'required': 'required'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        procurement_item = cleaned_data.get('procurement_item')
        amount = cleaned_data.get('amount')

        if procurement_item and amount:
            if procurement_item.amount <= 0:
                raise forms.ValidationError(f"OUT OF STOCK")
            if procurement_item.amount < amount:
                raise forms.ValidationError(f"NOT ENOUGH")
        return cleaned_data

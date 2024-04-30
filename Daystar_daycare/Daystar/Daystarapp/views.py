from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request, 'Daystarapp/index.html')
#@login_required(login_url='adminlogin')
def homes(request):
    count_babies = Babiesreg.objects.count()
    count_sitters = Sitterreg.objects.count()
    context={
        'count_babies': count_babies,
        'count_sitters': count_sitters,
    }
    return render(request, 'Daystarapp/home.html',{'context':context})
#@login_required(login_url='adminlogin')
def about(request):
    return render(request, 'Daystarapp/about.html')
#@login_required(login_url='adminlogin')
def addbabies(request):
    if request.method == 'POST':
        newbabyform = AddbabyForm(request.POST)
        if newbabyform.is_valid():
            newbabyform.save()
            return redirect('homes')
    else:
        newbabyform = AddbabyForm()
    return render(request, 'Daystarapp/babiesreg.html', {'newbabyform': newbabyform})
#@login_required(login_url='adminlogin')
def addsitter(request):
    if request.method == 'POST':
        addsitform = AddsitterForm(request.POST)
        if addsitform.is_valid():
            sitterloc = addsitform.cleaned_data['sitterloc']
            if sitterloc != 'Kabalagala':
              print("not suited for the job")
            else:
             addsitform.save()
             return redirect('homes')
    else:
        addsitform = AddsitterForm()
    return render(request, 'Daystarapp/sittersreg.html', {'addsitform': addsitform})
def addadmins(request):
    if request.method == 'POST':
        adminregform = AdminRegForm(request.POST)
        if adminregform.is_valid():
            adminregform.save()
            return redirect('adminlogin')
        else:
            messages.info(request, 'you have some invalid info')
    else:
        adminregform = AdminRegForm()
    return render(request, 'Daystarapp/adminreg.html', {'adminregform': adminregform})

def adminlogin(request):
    if request.method == 'POST':
        adminlogform = AdminloginForm(request.POST)
        if adminlogform.is_valid():
           username = adminlogform.cleaned_data.get('adminnamee')
           password = adminlogform.cleaned_data.get('adminpassw')
           user = authenticate(request, username=username, password=password)
           if user is not None:
             login(request, user)
             return redirect('homes')
        
           else:
               messages.info(request, 'user or password is incorrect')
        else:
            messages.info(request, 'you have some invalid info')
    else:
      adminlogform = AdminloginForm()
    return render(request, 'Daystarapp/adminlog.html', {'adminlogform': adminlogform})
#@login_required(login_url='adminlogin')    
def logoutuser(request):
    logout(request)
    return redirect('adminlogin')
#@login_required(login_url='adminlogin')  
def babyview(request):
    babies = Babiesreg.objects.all()
    return render(request, 'Daystarapp/babystatus.html', {'babies': babies})
#@login_required(login_url='adminlogin')
def sitterview(request):
    sitters = Sitterreg.objects.all()
    return render(request, 'Daystarapp/sitterstatus.html', {'sitters': sitters})

def payfor(request, tpay_id ):
    # Assuming you have instances of Sitterreg and you want to assign one of them to tpay field
    # Fetch the related instance of Sitterreg (assuming sitter_id is the primary key field)
    #sittername = Sitterreg.objects.get(sitterno=1)  # Replace some_id with the actual primary key value
    # Create an instance of Teachpayer and assign the related instance to tpay field
    #tname = Teachpayer(tpay=sittername)
    #tname.save()
    if request.method == 'POST':
        form = PaysForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = PaysForm()
    return render(request, 'Daystarapp/pay.html', {'form': form})
#@login_required(login_url='adminlogin')
def babydrop(request):
    if request.method == 'POST':
        dropbabyform = DropbabyForm(request.POST)
        if dropbabyform.is_valid():
            periodstay = dropbabyform.cleaned_data['periodstay']
            babypay = dropbabyform.cleaned_data['babypay'] 
            if periodstay == "full_day" and babypay == "15000" or periodstay == "half_day" and babypay == "10000":
                dropbabyform.save()
                return redirect('homes')
            elif periodstay == "half_day" and babypay == "15000" or periodstay == "full_day" and babypay == "15000":
                print("not accurate")

    else:
        dropbabyform = DropbabyForm()
    return render(request, 'Daystarapp/dropbaby.html', {'dropbabyform': dropbabyform})   

#@login_required(login_url='adminlogin')
def pickbaby(request):
    if request.method == 'POST':
        pickbabyform = PickbabyForm(request.POST)
        if pickbabyform.is_valid():
            pickbabyform.save()
            return redirect('homes')
    else:
        pickbabyform = PickbabyForm()
    return render(request, 'Daystarapp/babypick.html', {'pickbabyform': pickbabyform})
    


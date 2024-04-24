from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'Daystarapp/index.html')

def homes(request):
    return render(request, 'Daystarapp/homes.html')

def about(request):
    return render(request, 'Daystarapp/about.html')

def addbabies(request):
    Getbabyform = AddbabyForm()
    return render(request, 'Daystarapp/babiesreg.html', {'Getbabyform': Getbabyform})

def addsitter(request):
    Getsitterform = AddsitterForm()
    return render(request, 'Daystarapp/sittersreg.html', {'Getsitterform': Getsitterform})

def addadmins(request):
    Getadminregform = AdminregForm()
    return render(request, 'Daystarapp/adminreg.html', {'Getadminregform': Getadminregform})

def adminlogin(request):
    Getadminloginform = AdminloginForm()
    return render(request, 'Daystarapp/adminlog.html', {'Getadminloginform': Getadminloginform})
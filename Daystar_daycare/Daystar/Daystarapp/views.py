from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from django.dispatch import receiver

# Create your views here.
def index(request):
    return render(request, 'Daystarapp/index.html')
@login_required(login_url='index')
def homes(request):
    count_babies = Babiesreg.objects.count()
    count_sitters = Sitterreg.objects.count()
    count_toys = Sales.objects.count()
    count_pro = Procuregive.objects.count()
    count_assignbaby = Assignbaby.objects.count()
    count_pickbaby = Timeout.objects.count()
    return render(request, 'Daystarapp/home.html',{'count_babies':count_babies, 'count_sitters':count_sitters, 'count_toys':count_toys, 'count_pro':count_pro, 'count_assignbaby':count_assignbaby, 'count_pickbaby':count_pickbaby})
@login_required(login_url='index')
def about(request):
    return render(request, 'Daystarapp/about.html')
@login_required(login_url='index')
def addbabies(request):
    if request.method == 'POST':
        newbabyform = AddbabyForm(request.POST)
        if newbabyform.is_valid():
            periodstay = newbabyform.cleaned_data['period_of_stay']
            babypay = newbabyform.cleaned_data['babypay'] 
            if (periodstay == "fullday" and babypay == 15000) or (periodstay == "halfday" and babypay == 10000):
                newbabyform.save()
                return redirect('babyview')
            elif (periodstay == "halfday" and babypay == 15000) or (periodstay == "fullday" and babypay == 15000):
                messages.error(request, "THIS PAY DOES NOT MATCH THE PERIOD!!!")
            elif (periodstay == "monthly" and babypay != 450000):
                messages.error(request, "THIS PAY DOES NOT MATCH THE PERIOD!!!!")
    else:
        newbabyform = AddbabyForm()
    return render(request, 'Daystarapp/babiesreg.html', {'newbabyform': newbabyform})
@login_required(login_url='index')
def addsitter(request):
    if request.method == 'POST':
        addsitform = AddsitterForm(request.POST)
        if addsitform.is_valid():
            sitterloc = addsitform.cleaned_data['sitterloc']
            if sitterloc != 'Kabalagala':
              messages.error(request, "SITTER MUST STAY IN KABALAGALA!!!!")
            else:
             addsitform.save()
             return redirect('sitterview')
        else:
            messages.error(request, "FORM HAS SOME INVALID INFO!!!")
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
            messages.error(request, 'FORM HAS SOME INVALID INFO!!!')
    else:
        adminregform = AdminRegForm()
    return render(request, 'Daystarapp/adminreg.html', {'adminregform': adminregform})


"""def registeradmin(request):
    if request.method == 'POST':
        adminregform = AdminRegForm(request.POST)
        if adminregform.is_valid():
            adminregform.save()
            username = adminregform.cleaned_data['username']
            raw_password = adminregform.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('adminlogin')
        else:
            messages.info(request, 'you have some invalid info')
    else:
        adminregform = AdminRegForm()
    return render(request, 'Daystarapp/adminreg.html', {'adminregform': adminregform})"""



def adminlogin(request):
    if request.method == 'POST':
        adminlogform = AdminloginForm(request.POST)
        if adminlogform.is_valid():
           username = adminlogform.cleaned_data['username']
           password = adminlogform.cleaned_data['password']
           user = authenticate(request, username=username, password=password)
           if user is not None:
              login(request, user)
              return redirect('homes')
           else:
               messages.error(request, 'USERNAME OR PASSWOORD IS INCORRECT!!!')
        else:
            messages.info(request, 'FORM HAS SOME INVALID INFO!!!')
    else:
        adminlogform = AdminloginForm()
    return render(request, 'Daystarapp/adminlog.html', {'adminlogform': adminlogform})

def logoutuser(request):
    logout(request)
    return redirect('index')

@login_required(login_url='index')  
def babyview(request):
    babies = Babiesreg.objects.all()
    return render(request, 'Daystarapp/babystatus.html', {'babies': babies})

@login_required(login_url='index')
def sitterview(request):
    sitters = Sitterreg.objects.all()
    return render(request, 'Daystarapp/sitterstatus.html', {'sitters': sitters})

#def payfor(request, tpay_id ):
    # Assuming you have instances of Sitterreg and you want to assign one of them to tpay field
    # Fetch the related instance of Sitterreg (assuming sitter_id is the primary key field)
    #sittername = Sitterreg.objects.get(sitterno=1)  # Replace some_id with the actual primary key value
    # Create an instance of Teachpayer and assign the related instance to tpay field
    #tname = Teachpayer(tpay=sittername)
    #tname.save()
    #if request.method == 'POST':
        #form = PaysForm(request.POST)
       # if form.is_valid():
            #form.save()
            #return redirect('/home')
   #else:
       #form = PaysForm()
    #return render(request, 'Daystarapp/pay.html', {'form': form}
@login_required(login_url='index')
def pickbaby(request):
    if request.method == 'POST':
        pickbabyform = PickbabyForm(request.POST)
        if pickbabyform.is_valid():
            pickbabyform.save()
            return redirect('babypickview')
        else:
            messages.error(request, "FORM HAS SOME INVALID INFO!!!")
    else:
        pickbabyform = PickbabyForm()
    return render(request, 'Daystarapp/babypick.html', {'pickbabyform': pickbabyform})

@login_required(login_url='index')
def regdoll(request):
    if request.method == 'POST':
        regdollform = DollRegForm(request.POST)
        if regdollform.is_valid():
            regdollform.save()
            return redirect('dolltotalview')
        else:
         messages.error(request, "FORM HAS SOME INVALID INFO!!!")
    else:
        regdollform = DollRegForm()
    return render(request, 'Daystarapp/dollreg.html', {'regdollform': regdollform})

@login_required(login_url='index')
def sales_view(request):
    if request.method == 'POST':
        sellform = SalesForm(request.POST)
        if sellform.is_valid():
            sellform.save()

            return redirect('salerecord')
        else:
            messages.error(request, "FORM HAS SOME INVALID INFO!!!")
    else:
        sellform = SalesForm()
    return render(request, 'Daystarapp/sales.html', {'sellform': sellform})


@login_required(login_url='index')
def salerecord(request):
    #salee = Sales.objects.get(id=sale_id)
    sale = Sales.objects.all()
    return render(request, 'Daystarapp/salerecord.html', {'sale': sale})

@login_required(login_url='index')
def editsitterview(request, id):
    sitter = Sitterreg.objects.get(id=id)
    if request.method == 'POST':
        sitterform = AddsitterForm(request.POST, instance = sitter)
        if sitterform.is_valid():
            sitterform.save()
            return redirect('sitterview')
        else:
            messages.error(request, "FORM HAS SOME INVALID INFO!!!")
    else:
        sitterform = AddsitterForm(instance = sitter)
        return render(request, 'Daystarapp/sittersreg.html', {'addsitform': sitterform})
    
@login_required(login_url='index')
def deletesitterview(request, id):
    siter = Sitterreg.objects.get(pk=id)
    siter.delete()
    return redirect('sitterview')

@login_required(login_url='index')
def editbabyview(request, id):
    babys = Babiesreg.objects.get(id=id)
    if request.method == 'POST':
        babyform = AddbabyForm(request.POST, instance = babys)
        if babyform.is_valid():
            babyform.save()
            return redirect('babyview')
        else:
            messages.error(request, "FORM HAS SOME INVALID INFO!!!")
    else:
        babyform = AddbabyForm(instance = babys)
        return render(request, 'Daystarapp/babiesreg.html', {'newbabyform': babyform})
    
@login_required(login_url='index')
def deletebabyview(request, id):
    baby = Babiesreg.objects.get(pk=id)
    baby.delete()
    return redirect('babyview')

@login_required(login_url='index')
def assignbabyview(request):
    if request.method == 'POST':
        assignform = AssignbabyForm(request.POST)
        if assignform.is_valid():
            attendance = assignform.cleaned_data['attendance']
            if attendance == "Present":
                assignform.save()
                return redirect('assignrec')
            else:
                messages.error(request, "SITTER IS REQUIRED TO BE PRESENT!!!")
        else:
            messages.error(request, "FORM HAS SOME INVALID INFO!!!")
    else:
        assignform = AssignbabyForm()
    return render(request, 'Daystarapp/assign.html', {'assignform': assignform}) 
  
@login_required(login_url='index')
def assignrec(request):
    assign = Assignbaby.objects.all()
    return render(request, 'Daystarapp/assignrecord.html', {'assign': assign})


@login_required(login_url='index')
def procure_view(request):
    if request.method == 'POST':
        proform = ProcurementForm(request.POST)
        if proform.is_valid():
            proform.save()
            return redirect('prototalview')
        else:
            messages.error(request, "FORM HAS SOME INVALID INFO!!!")
    else:
        proform = ProcurementForm()
    return render(request, 'Daystarapp/procure.html', {'proform': proform})

@login_required(login_url='index')
def procuregive(request):
    if request.method == 'POST':
        progiveform = ProcurementgiveForm(request.POST)
        if progiveform.is_valid():
            progiveform.save()
            return redirect('procure_record')
        else:
            messages.error(request, "FORM HAS SOME INVALID INFO!!!")
    else:
        progiveform = ProcurementgiveForm()
    return render(request, 'Daystarapp/procuregive.html', {'progiveform': progiveform})




@login_required(login_url='index')
def procure_record(request):
    procure = Procuregive.objects.all()
    return render(request, 'Daystarapp/procurerec.html', {'procure': procure})

@receiver(post_save, sender=Sales)
def update_dolls_quantity(sender, instance, created, **kwargs):
   if created:
       instance.doll_item.quantity -= instance.quantity
       instance.doll_item.save()

@receiver(post_save, sender=Procuregive)
def update_procure_quantity(sender, instance, created, **kwargs):
    if created:
        instance.procurement_item.amount -= instance.amount
        instance.procurement_item.save()

@login_required(login_url='index')
def babypickview(request):
    babiespick = Timeout.objects.all()
    return render(request, 'Daystarapp/pickrec.html', {'babiespick': babiespick})

@login_required(login_url='index')
def prototalview(request):
    prototal = Procure.objects.all()
    return render(request, 'Daystarapp/prooverall.html', {'prototal': prototal})

@login_required(login_url='index')
def dolltotalview(request):
    dolltotal = Dollstall.objects.all()
    return render(request, 'Daystarapp/dolloverall.html', {'dolltotal': dolltotal})

@login_required(login_url='index')
def editdollview(request, id):
    dolls = Dollstall.objects.get(id=id)
    if request.method == 'POST':
        dollform = DollRegForm(request.POST, instance = dolls)
        if dollform.is_valid():
            dollform.save()
            return redirect('dolltotalview')
        else:
            messages.info(request, "FORM HAS SOME INVALID INFO!!!")
    else:
        dollform = DollRegForm(instance = dolls)
        return render(request, 'Daystarapp/dollreg.html', {'regdollform': dollform})
    
@login_required(login_url='index')
def deletedollview(request, id):
    doll = Dollstall.objects.get(pk=id)
    doll.delete()
    return redirect('dolltotalview')

@login_required(login_url='index')
def editproview(request, id):
    pros = Procure.objects.get(id=id)
    if request.method == 'POST':
        prosform = ProcurementForm(request.POST, instance = pros)
        if prosform.is_valid():
            prosform.save()
            return redirect('prototalview')
        else:
            messages.error(request, "FORM HAS SOME INVALID INFO!!!")
    else:
        prosform = ProcurementForm(instance = pros)
        return render(request, 'Daystarapp/procure.html', {'proform': prosform})
    
@login_required(login_url='index')
def deleteproview(request, id):
    pro = Procure.objects.get(pk=id)
    pro.delete()
    return redirect('prototalview')

@login_required(login_url='index')
def deletesaleview(request, id):
    pro = Sales.objects.get(pk=id)
    pro.delete()
    return redirect('salerecord')
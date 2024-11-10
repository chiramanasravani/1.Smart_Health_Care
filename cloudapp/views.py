from django.shortcuts import render

# Create your views here.


from turtle import down
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from userapp.models import *
from mainapp.models import *
from cloudapp.models import *

from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404



from django.core.mail import EmailMultiAlternatives
from smartproject.settings import DEFAULT_FROM_EMAIL
from mainapp.check_internet import *
from networkapp.models import *
from mainapp.check_internet import *
from networkapp.models import *
from protectionapp.models import *
# from Power.settings import DEFAULT_FROM_EMAIL
# import pandas as pd

def cloud_login(request):
    if request.method=='POST':
        name=request.POST.get('name')
        pwd=request.POST.get('pwd')
        if name=='cloud' and pwd=='cloud':
            messages.info(request,"login successfull")
            return redirect('cloud_dashboard')
        else:
            messages.warning(request,'Something Wrong, Please try again.')
            print('message')
            return redirect ('cloud_login')
    return render(request,'main/cloud-login.html')



def cloud_dashboard(request):
    users=userModel.objects.count()
    device=deviceModel.objects.count()
    phi=phiModel.objects.count()
    data1 = phiModel.objects.filter(status='Pending').count()
    print(data1)
    data2 = phiModel.objects.filter(phi_status="Pending").count()
    print(data2)
    data3 = deviceModel.objects.filter(device_status='Pending').count()
    return render(request,'cloud/cloud-dashboard.html',{'users':users,'device':device,'phi':phi,'data1':data1,'data2':data2,'data3':data3})
    #


def cloud_view_phi(request):
    data=phiModel.objects.filter().order_by("-phi_id")
    if request.method=='POST':
         search=request.POST.get('search')
         data=phiModel.objects.filter(Q(phi_id__icontains=search))
    return render(request,'cloud/cloud-view-phi.html',{'data':data})    
   


def accept_phi(request,id):
    accept=get_object_or_404(phiModel,phi_id=id)
    accept.status='Accepted'
    accept.save(update_fields=['status'])
    accept.save()
    return redirect('cloud_view_phi')

def reject_phi(request,id):
    reject=get_object_or_404(phiModel,phi_id=id)
    reject.status='Rejected'
    reject.save(update_fields=['status'])
    reject.save()
    return redirect('cloud_view_phi')      
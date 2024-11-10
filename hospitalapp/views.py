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
import requests
import random
import numpy as np
import matplotlib.pyplot as plt

from django.core.mail import EmailMultiAlternatives
from smartproject.settings import DEFAULT_FROM_EMAIL
from mainapp.check_internet import *
from networkapp.models import *
from mainapp.check_internet import *
from networkapp.models import *
from protectionapp.models import *
# from Power.settings import DEFAULT_FROM_EMAIL
# import pandas as pd

def sd_login(request):
    if request.method=='POST':
        name=request.POST.get('name')
        pwd=request.POST.get('pwd')
        if name=='sd' and pwd=='sd':
            messages.info(request,"login successfull")
            return redirect('sd_dashboard')
        else:
            messages.warning(request,'Something Wrong, Please try again.')
            print('message')
            return redirect ('sd_login')
    return render(request,'main/sd-login.html')



def sd_dashboard(request):
    users=userModel.objects.count()
    device=deviceModel.objects.count()
    phi=phiModel.objects.count()
    data1 = phiModel.objects.filter(status='Pending').count()
    print(data1)
    data2 = phiModel.objects.filter(phi_status="Pending").count()
    print(data2)
    data3 = deviceModel.objects.filter(device_status='Pending').count()
    return render(request,'service-divice/sd-dashboard.html',{'users':users,'device':device,'phi':phi,'data1':data1,'data2':data2,'data3':data3})

def sd_view_phi_data_details(request):
    data=phiModel.objects.filter(status="Accepted").order_by("-phi_id")

    if request.method=='POST':
         search=request.POST.get('search')
         data=phiModel.objects.filter(Q(phi_id__icontains=search))
    
    return render(request,'service-divice/sd-view-phi-data-details.html',{'data':data})    


def phi_status(request,id):
    phiModel.objects.filter(phi_id=id)
    obj=get_object_or_404(phiModel,phi_id=id)
   
    print("fffffffffffffffffffffffffffffffff")
    if request.method=='POST' and request.FILES['prescription']:
       
        description=request.POST['description']
        print(description)
        prescription=request.FILES['prescription']
        print(prescription)
        obj.prescription=prescription
        obj.description=description
       
        obj.prescription=prescription
        obj.save(update_fields=['prescription','description'])
        obj.save()

        phiModel.objects.filter(phi_id=id).update(phi_status='sended')

        messages.info(request,'prescription Sended Successfully.')
        return redirect('sd_view_phi_data_details')
    return render(request,'service-divice/phi-status.html')    

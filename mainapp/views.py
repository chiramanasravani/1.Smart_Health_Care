
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
from django.db.models import Q, F, Sum
from cryptography.fernet import Fernet
import random



# Create your views here.


def home(request):
    users=userModel.objects.count()
    device=deviceModel.objects.count()
    phi=phiModel.objects.count()
    data1 = phiModel.objects.filter(status='Pending').count()

    data4 = phiModel.objects.filter(phi_status='Sended').count()

    print(data1)
    data2 = phiModel.objects.filter(status="Sended").count()
    print(data2)
    data3 = deviceModel.objects.filter(device_status='Pending').count()
    
    return render(request,'main/index.html',{'users':users,'device':device,'phi':phi,'data1':data1,'data2':data2,'data3':data3,'data4':data4})


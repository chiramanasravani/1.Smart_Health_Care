from re import L
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
from django.db.models import Q, F, Sum
from cryptography.fernet import Fernet
import random
import time
import sys
from tqdm import tqdm
import win32file
import win32
import win32api








# Create your views here.

ALLOWED_EXTENSIONS=set(['txt','py','html','java','js'])


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        password = request.POST.get('password')
        print(password)

        try:
            check = userModel.objects.get(email=email,password=password)
            print(check)
            request.session["user_id"] = check.user_id
            messages.info(request,"Login Successfully")
            return redirect('user_dashboard')
            
        
        except:
            messages.warning(request,"Invalid username or password")
            return redirect('user_login')


    return render(request,'user/user-login.html')


#user register
def user_register(request):
    if request.method=='POST' and request.FILES['user_image']:
        user_name=request.POST ['user_name']
        print(user_name) 
        email=request.POST['email']       
        password=request.POST['password']
        mobile=request.POST['mobile']
        dob=request.POST['dob']
        location=request.POST['location']
        user_image=request.FILES['user_image']


        if userModel.objects.filter(email=email).filter(verification = "verified"):
            messages.warning(request,"Email  Already  Exists!")
            print("Already")
        elif userModel.objects.filter(email=email).filter(verification = "Pending"):
            messages.warning(request,"Already Rejistered, Just verify your account!")
            otp=random.randint(2222,4444)
            userModel.objects.filter(email=email,verification='Pending').update(otp=otp)
            url = "https://www.fast2sms.com/dev/bulkV2"
            # create a dictionary
            my_data = {'sender_id': 'FSTSMS', 
                        'message': 'Welcome to Dual Access Control in Cloud, your verification OPT is '+str(otp)+'Thanks for request of OTP.', 
                        'language': 'english', 
                        'route': 'p', 
                        'numbers': mobile
            }

            # create a dictionary
            headers = {
                'authorization': 'D4vuFnk1sNQOl6SRpfZUT23ewPX0BoLrzAJVgqtW8bxyHEGjImfkE0NtULg1TG9xImYHpVZjQMnBSOoa',
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache"
            }
            
            if connect():

            # make a post request
                response = requests.request("POST",
                                            url,
                                            data = my_data,
                                            headers = headers)
            
                print(response.text)      
            return redirect('user_otp')  

        else:
            print("vssdvsdvsd")
            otp=random.randint(2222,4444)
            url = "https://www.fast2sms.com/dev/bulkV2"
            # create a dictionary
            my_data = {'sender_id': 'FSTSMS', 
                        'message': 'Welcome to CloudHost, your verification OPT is '+str(otp)+'Thanks for request of OTP.', 
                        'language': 'english', 
                        'route': 'p', 
                        'numbers': mobile
            }

            # create a dictionary
            headers = {
                'authorization': 'D4vuFnk1sNQOl6SRpfZUT23ewPX0BoLrzAJVgqtW8bxyHEGjImfkE0NtULg1TG9xImYHpVZjQMnBSOoa',
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache"
            }

            if connect():
            # make a post request
                response = requests.request("POST",
                                            url,
                                            data = my_data,
                                            headers = headers)
            
                print(response.text)        

            userModel.objects.create(user_name=user_name,password=password,mobile=mobile,email=email,dob=dob,location=location,user_image=user_image,otp=otp)
            messages.success(request,'Account Created Successfully!')
            return redirect('user_otp')
    return render(request,'user/user-register.html')

def user_otp(request):
    # user_id=request.session['user_id']

    if request.method == "POST":
        otp = request.POST.get('otp')
        print(otp)
        try:
            print('ppppppppppppppppppppp')
            check = userModel.objects.get(otp=otp)
            user_id = request.session['user_id']=check.user_id
            otp=check.otp
            print(otp)
            if otp == otp:
                userModel.objects.filter(user_id=user_id).update(verification='Verified')
                messages.info(request,'Account Created Successfully!')
                return redirect('user_login')
            else:
                return redirect('user_otp')
        except:
            pass
    return render(request,'user/user-otp.html')
        


def user_dashboard(request):
    
    user_id=request.session["user_id"]
    device=deviceModel.objects.filter(user_id=user_id).values('device_id').count()

    phi=phiModel.objects.filter(user_id=user_id).filter(phi_status='Pending').count()

    data1 = phiModel.objects.filter(user_id=user_id).filter(phi_status='Sended').count()
    data4 = phiModel.objects.filter(phi_status='Sended').count()

    print(data1)
    data2 = phiModel.objects.filter(status="Sended").count()
    print(data2)
    data3 = deviceModel.objects.filter(device_status='Pending').count()
    

    return render(request,'user/user-dashboard.html',{'device':device,'phi':phi,'data1':data1,'data2':data2,'data3':data3,'data4':data4})
# 
def locate_usb():
    drive_list = []
    drivebits = win32file.GetLogicalDrives()
    for d in range(1, 26):
        mask = 1 << d
        if drivebits & mask:
            # here if the drive is at least there
            drname = '%c:\\' % chr(ord('A') + d)
            t = win32file.GetDriveType(drname)
            if t == win32file.DRIVE_REMOVABLE:
                drive_list.append(drname)
    return drive_list


def user_add_phi(request):


   


     
        # context = pyudev.Context()
        # monitor = Monitor.from_netlink()
        # # For USB devices
        # monitor.filter_by(susbsytem='usb')
        # # OR specifically for most USB serial devices
        # monitor.filter_by(susbystem='tty')
        # for action, device in monitor:
        # vendor_id = device.get('ID_VENDOR_ID')

        # if vendor_id in ['USB\\VID_0930&PID_6544&REV_0100'] or vendor_id in ['USB\\VID_0930&PID_6544']:
        #  print ('Detected {0} for device with vendor ID {1}'.format(action, vendor_id))

    
    # context = pyudev.Context()
    # monitor = Monitor.from_netlink()
    # # For USB devices
    # monitor.filter_by(susbsytem='usb')
    # # OR specifically for most USB serial devices
    # monitor.filter_by(susbystem='tty')
    # for action, device in monitor:
    #     vendor_id = device.get('ID_VENDOR_ID')
    # # I know the devices I am looking for have a vendor ID of '22fa'
    # if vendor_id in ['22fa']:
    #     print('Detected {} for device with vendor ID {}'.format(action, vendor_id))


    user_id=request.session['user_id']
    device_id=request.session['device_id']

    

    device=deviceModel.objects.get(device_id=device_id)
    device_type=device.device_type
    print(device)
    print('_typeeeeeeeeeeeeeeeeeeeeeeeeee')
    
    # phi=deviceModel.objects.filter(device_id=device_id).filter(device_status='Pending')
    
    try:  
        print(device_id)
        check = phiModel.objects.get(device_id=device_id)
        print(check)

        
        print("wronggggggggggggggggggggggggggggggggggggg")
        
        messages.warning(request,"Please Add the Device First")
        return redirect('user_add_divice')
            
        
    except:
            pass

    if request.method=='POST':
        patient_name=request.POST ['patient_name']
        print(patient_name)
        
        weight=request.POST['weight']   
        print(weight)     
        height=request.POST['height']
        blood_group=request.POST['blood_group']
        age=request.POST['age']
       
        print("chanuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")


        drive_list = win32api.GetLogicalDriveStrings()
        print('ffffffffffffffffffffffffffffffffffff')
        drive_list = drive_list.split("\x00")[0:-1]
        print(drive_list)  # the last element is ""
        success='B'
        for letter in drive_list:
            print('type',win32file.GetDriveType(letter))
            print('removable',win32file.DRIVE_REMOVABLE)
            print('ddddddddddddddddddddddddddddddddddddd',letter)
            if win32file.GetDriveType(letter) == win32file.DRIVE_REMOVABLE:# check if the drive is of type removable 
                print("list drives: {0}".format(letter))
                success='A'

        if success !='A':
            messages.warning(request,'Please Connect The Device.')
            return redirect('user_add_phi')

            # else:
            #     print("sssssssssssssssssssssssssssssssssssss")

            #     messages.warning(request,'Please Connect The Device.')
            #     return redirect('user_add_phi')
    
        

        if deviceModel.objects.filter(user_id=user_id).filter(key_status='Pending'):
         messages.warning(request,'Protection Key Status is Still Pending! Please Wait ...!')
         return redirect('user_dashboard')

        else:
        
            # animation = "|/-\\"

            # for i in range(100):
            #     time.sleep(0.1)
            #     sys.stdout.write("\r" + animation[i % len(animation)])
            #     sys.stdout.flush()
            #     #do something
            #     print("End!")

            check=phiModel.objects.create(patient_name=patient_name,weight=weight,height=height,blood_group=blood_group,age=age,user_id=user_id,device_id=device_id,device_name=device_type)
            print(check)
            request.session["phi_id"] = check.phi_id

       



        # user_id=phi.user_id
        # print(user_id)
        # print("user_id:------------------------------",user_id)
        
       
        messages.info(request,'PHI Aded Successfully.')
        return redirect('user_health_details')
    return render(request,'user/user-add-phi.html',{'device_type':device_type})



def user_add_divice(request):
    user_id=request.session['user_id']
   
   
    print(user_id)
    print("ssssssssssssssssssssssssssssssssssssss")
    # data=deviceModel.objects.filter(user_id=user_id)
    if request.method=='POST':
        device_name=request.POST['device_name']
        print('device name-------------------',device_name)
        print("ssssssssssssssssssssssssssssssssssssss")
        
        device_type=request.POST['device_type']   
        print("divice type", device_type)   
        
       
        device=deviceModel.objects.create(device_name=device_name,device_type=device_type,user_id=user_id)
        request.session["device_id"] = device.device_id
        print(request.session["device_id"])
        messages.info(request,'Device Aded Successfully.')
        return redirect('user_add_phi')
    return render(request,'user/user-add-device.html')




def user_doctor_responce(request):
    user_id=request.session['user_id']
    phi=phiModel.objects.filter(user_id=user_id,phi_status="sended")
  
    return render(request,'user/user-doctor-responce.html',{'phi':phi})



def user_health_details(request):
    phi_id=request.session['phi_id']
    phi_id=phiModel.objects.get(phi_id=phi_id)
    print(phi_id)    

    return render(request,'user/user-health-details.html',{'phi_id':phi_id})





def user_details(request,id):

    # for i in tqdm (range (100), desc="Loading..."):
    #     pass

    # toolbar_width = 50

    # # setup toolbar
    # sys.stdout.write("[%s]" % (" " * toolbar_width))
    # sys.stdout.flush()
    # sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

    # for i in range(toolbar_width):
    #     time.sleep(0.1) # do real work here
    #     # update the bar
    #     sys.stdout.write("-")
    #     sys.stdout.flush()

    # sys.stdout.write("]\n") # this ends the progress bar

     #    Returns a list containing letters from removable drives
   



    bp1=['120/80','120/50','120/60','120/90']
    bp=(random.choice(bp1))

    oxyzen1=['70%','80%','90%','60%','50%']
    oxyzen=(random.choice(oxyzen1))

    sugar1=['70-100','70-140','70-160 °','70-150']
    sugar=(random.choice(sugar1))

    body_temp1=['98.6° F','37 ° F','36° F','35° F']
    body_temp=(random.choice(body_temp1))

    # pulserate1=['70','80%','90%','60%','50%']
    # pulserate=(random.choice(pulserate1))

    # bmp1=['70-100','70/140','70/160','70/150']
    # bmp=(random.choice(bmp1))

    # body_temp1=['70%','80%','90%','60%','50%']
    # body_temp=(random.choice(body_temp1))


    # sugar=random.uniform(1,8)
    pulserate=random.randint(70,72)
    bmp=random.randint(30,99)
    # body_temp=random.randint(00,99)   
    obj=get_object_or_404(phiModel,phi_id=id)
    print(obj)
   
    print("fffffffffffffffffffffffffffffffff")
    if request.method=='POST' :
        print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        
       
        oxyzen=request.POST['oxyzen']
        print(oxyzen)
        pulserate=request.POST['pulserate']
        body_temp=request.POST['body_temp']
        bmi=request.POST['bmi']
        bp=request.POST['bp']
        print(bmi)
        sugar=request.POST['sugar']
        print(sugar)
       
       
        obj.pulserate=pulserate
        obj.sugar=sugar
        obj.bp=bp
        obj.oxyzen=oxyzen
        obj.body_temp=body_temp
        obj.bmi=bmi
        obj.save(update_fields=['pulserate','sugar','bp','oxyzen','body_temp','bmi'])
        obj.save()

        # phiModel.objects.filter(phi_id=id).update(phi_status='sended')

        messages.info(request,'PHI details Sended Successfully.')
        return redirect('user_dashboard')
    return render(request,'user/user-details.html',{'bp':bp,'sugar':sugar,'pulserate':pulserate,'bmp':bmp,'body_temp':body_temp,'oxyzen':oxyzen})
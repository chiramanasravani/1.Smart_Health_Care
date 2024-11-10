"""smartproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ast import If
from xml.dom.minidom import Document


from django.conf.urls.static import static
from django.conf import settings
from cloudapp import views as cloudapp_views
from userapp import views as userapp_views
from mainapp import views as mainapp_views
from networkapp import views as networkapp
from hospitalapp import views as hospitalapp
from protectionapp import views as protectionapp




urlpatterns = [
    path('admin/', admin.site.urls),

    path('',mainapp_views.home,name='home'),


# cloud

    path('cloud-login',cloudapp_views.cloud_login,name='cloud_login'),

    path('cloud-dashboard', cloudapp_views.cloud_dashboard,name='cloud_dashboard'),

    path('cloud-view-phi',cloudapp_views.cloud_view_phi,name='cloud_view_phi'),

    path('accept-phi/<int:id>/',cloudapp_views.accept_phi,name='accept_phi'),
    
    path('reject-phi/<int:id>/',cloudapp_views.reject_phi,name='reject_phi'),

   

    # path('accept-status/<int:id>/',cloudapp_views.reject_status,name='reject_status'),

#network manager


    path('nm-login',networkapp.nm_login,name='nm_login'),

    path('nm-dashboard', networkapp.nm_dashboard,name='nm_dashboard'),

    path('nm-view-pad-details', networkapp.nm_view_pad_details,name='nm_view_pad_details'),

    path('accept-status/<int:id>/',networkapp.accept_status,name='accept_status'),


# key protection server


    path('kp-login',protectionapp.kp_login,name='kp_login'),

    path('kp-dashboard', protectionapp.kp_dashboard,name='kp_dashboard'),

    path('kp-view-pad-details', protectionapp.kp_view_pad_details,name='kp_view_pad_details'),

    path('device-status/<int:id>/',protectionapp.device_status,name='device_status'),


#Service divice


    path('sd-login',hospitalapp.sd_login,name='sd_login'),

    path('sd-dashboard', hospitalapp.sd_dashboard,name='sd_dashboard'),

    path('sd-view-phi-data-details', hospitalapp.sd_view_phi_data_details,name='sd_view_phi_data_details'),

    path('phi-status/<int:id>/',hospitalapp.phi_status,name='phi_status'),



#user


    path('user-otp',userapp_views.user_otp,name='user_otp'),

    path('user-login',userapp_views.user_login,name='user_login'),

    path('user-register', userapp_views.user_register,name='user_register'),

    path('user-dashboard', userapp_views.user_dashboard,name='user_dashboard'),

    path('user-add-phi',userapp_views.user_add_phi,name='user_add_phi'),

    path('user-add-divice',userapp_views.user_add_divice,name='user_add_divice'),

    path('user-doctor-responce',userapp_views.user_doctor_responce,name='user_doctor_responce'),

    path('user-details/<int:id>/',userapp_views.user_details,name='user_details'),

    path('user-health-details',userapp_views.user_health_details,name='user_health_details'),
   
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
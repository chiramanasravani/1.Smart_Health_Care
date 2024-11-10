from django.db import models

# Create your models here.
class userModel(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(help_text='user_name',max_length=50)
    email=models.EmailField(help_text=' email', max_length=50)
    password=models.CharField(help_text='password', max_length=50)
    mobile=models.BigIntegerField(help_text='mobile')
    location=models.CharField(help_text='location', max_length=200)
    dob=models.DateField(help_text='dob')
    user_image=models.ImageField(upload_to='user_image/', null=True)
    otp=models.IntegerField(null=True)
    verification=models.CharField(max_length=50,default='Pending')
    status=models.CharField(max_length=50,default='Pending',null="True")
    reg_date=models.DateField(auto_now_add=True)

    class Meta:
        db_table='user_details'



class phiModel(models.Model):
    phi_id=models.AutoField(primary_key=True)
    # vm=models.ForeignKey(vmModel,db_column='vm_id', related_name='vm',on_delete=models.CASCADE,null=True,blank=True)
    user_id=models.IntegerField(null=True)
    device_id=models.IntegerField(null=True)
    patient_name=models.CharField(help_text='patient_name',max_length=200)
    weight=models.CharField(help_text='weight',max_length=250, null=True)
    height=models.CharField(help_text='height',max_length=250, null=True)
    age=models.CharField(help_text='age',max_length=250, null=True)
    blood_group=models.CharField(help_text='blood_group',max_length=300)
    status=models.CharField(max_length=50,null="True",default='Pending')
    phi_status=models.CharField(max_length=50,null="True",default='Pending')
    prescription=models.ImageField(upload_to='prescription/',null="True")
    description=models.CharField(max_length=50,null="True",default='Pending')
    device_name=models.CharField(max_length=50,null="True",default='Pending')
    phi_uploaded_date=models.DateField(auto_now_add=True, null=True)


    bp=models.CharField(max_length=50,null="True")
    sugar=models.CharField(max_length=50,null="True")
    pulserate=models.CharField(max_length=50,null="True")
    oxyzen=models.CharField(max_length=50,null="True")
    bmi=models.CharField(max_length=50,null="True")
    body_temp=models.CharField(max_length=50,null="True")


    class Meta:
        db_table='PHI_details'         

class deviceModel(models.Model):
    device_id=models.AutoField(primary_key=True)
    user_id=models.IntegerField(null=True)
    device_name=models.CharField(help_text='device_name',max_length=200)
    device_type=models.CharField(help_text='device_type',max_length=250, null=True)
    key_status=models.CharField(max_length=50,null="True",default='Pending')
    device_status=models.CharField(max_length=50,null="True",default='Pending')
    device_uploaded_date=models.DateField(auto_now_add=True, null=True)
    nm_key=models.CharField(null=True,max_length=200)
    pt_key=models.CharField(null=True,max_length=200)

    

    class Meta:
        db_table='device_details'         


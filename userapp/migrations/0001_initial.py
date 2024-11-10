# Generated by Django 4.0.4 on 2022-06-29 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='deviceModel',
            fields=[
                ('device_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(null=True)),
                ('device_name', models.CharField(help_text='device_name', max_length=200)),
                ('device_type', models.CharField(help_text='device_type', max_length=250, null=True)),
                ('key_status', models.CharField(default='Pending', max_length=50, null='True')),
                ('device_status', models.CharField(default='Pending', max_length=50, null='True')),
                ('device_uploaded_date', models.DateField(auto_now_add=True, null=True)),
                ('file_key', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'device_details',
            },
        ),
        migrations.CreateModel(
            name='phiModel',
            fields=[
                ('phi_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(null=True)),
                ('patient_name', models.CharField(help_text='patient_name', max_length=200)),
                ('weight', models.CharField(help_text='weight', max_length=250, null=True)),
                ('height', models.CharField(help_text='height', max_length=250, null=True)),
                ('age', models.CharField(help_text='age', max_length=250, null=True)),
                ('blood_group', models.CharField(help_text='blood_group', max_length=300)),
                ('status', models.CharField(default='Pending', max_length=50, null='True')),
                ('phi_status', models.CharField(default='Pending', max_length=50, null='True')),
                ('prescription', models.ImageField(null='True', upload_to='files/')),
                ('description', models.CharField(default='Pending', max_length=50, null='True')),
                ('phi_uploaded_date', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'PHI_details',
            },
        ),
        migrations.CreateModel(
            name='userModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(help_text='user_name', max_length=50)),
                ('email', models.EmailField(help_text=' email', max_length=50)),
                ('password', models.CharField(help_text='password', max_length=50)),
                ('mobile', models.BigIntegerField(help_text='mobile')),
                ('location', models.CharField(help_text='location', max_length=200)),
                ('dob', models.DateField(help_text='dob')),
                ('user_image', models.ImageField(null=True, upload_to='user_image/')),
                ('otp', models.IntegerField(null=True)),
                ('verification', models.CharField(default='Pending', max_length=50)),
                ('status', models.CharField(default='Pending', max_length=50, null='True')),
                ('reg_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'user_details',
            },
        ),
    ]
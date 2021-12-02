# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-2#se2w2t^20h%7g6_6+(zztxlmz#99f*r(dgsri7@ip_8zov@'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'capstone_database',
        'USER': 'root',
        'PASSWORD': 'IloveBeau123!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db.models.deletion import CASCADE

    

class EmployeeRoles(models.Model):
    labour_code = models.CharField(max_length=50)

class Employees(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    labour_code=ForeignKey(EmployeeRoles, on_delete=models.CASCADE)

class JobList(models.Model):
    job_name = models.CharField(max_length=400)
    job_site = models.CharField(max_length=400)
    job_start_date= models.IntegerField(blank= True, null=True)
    job_end_date= models.IntegerField(blank= True, null=True)
    business_name= models.ForeignKey(Owner, on_delete=models.CASCADE)

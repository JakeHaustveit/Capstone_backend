from enum import unique
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db.models.deletion import CASCADE

# Create your models here.

class Owner(models.Model):
    business_name = models.CharField(max_length=50, unique = True)
    user = models.ForeignKey('authentication.User', blank= True, null= True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class JobList(models.Model):
    job_name = models.CharField(max_length=100)
    job_site = models.CharField(max_length=100)
    job_start_date= models.DateField
    job_end_date= models.DateField
    business_name= models.ForeignKey(Owner, to_field='business_name', on_delete=models.CASCADE)

class EmployeeRoles(models.Model):
    labor_code = models.CharField(max_length = 50, unique = True)
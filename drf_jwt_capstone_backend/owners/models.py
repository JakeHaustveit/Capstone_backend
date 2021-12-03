from enum import unique
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.

class Owners(models.Model):
    business_name = models.CharField(max_length=50, unique = True)
    user = models.ForeignKey(User, blank = True, null = True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class JobList(models.Model):
    job_name = models.CharField(max_length=100)
    job_site = models.CharField(max_length=100)
    job_start_date= models.DateField(blank = True, null = True)
    job_end_date= models.DateField(blank = True, null = True)
    business_name= models.ForeignKey(Owners, to_field='business_name', on_delete=models.CASCADE)

class EmployeeRoles(models.Model):
    labor_code = models.CharField(max_length = 50, unique = True)
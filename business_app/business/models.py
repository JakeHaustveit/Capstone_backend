from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db.models.deletion import CASCADE

# Create your models here.
class Owner(models.Model):
    business_name = models.CharField(max_length=400)
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    employee_login_code = models.CharField(max_length=400)

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



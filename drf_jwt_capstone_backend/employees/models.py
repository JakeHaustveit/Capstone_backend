from enum import unique
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
from owners.models import JobList
from owners.models import EmployeeRoles
User = get_user_model()

# Create your models here.

class Employees(models.Model):    
    username=models.ForeignKey(User, to_field="username", on_delete = models.CASCADE)
    vacation_start_date=models.DateField(blank = True, null = True)
    vacation_end_date=models.DateField(blank = True, null = True)

    


class EmployeesWorkSchedule(models.Model):
    username = models.ForeignKey(User, to_field="username", on_delete=CASCADE)
    area_working =models.ForeignKey(JobList, to_field="job_name", on_delete=CASCADE, blank = True, null = True)
    labor_code= ForeignKey(EmployeeRoles, to_field="labor_code", on_delete = models.CASCADE)    
    date_worked = models.DateField()
    start_time= models.TimeField()
    end_time= models.TimeField()
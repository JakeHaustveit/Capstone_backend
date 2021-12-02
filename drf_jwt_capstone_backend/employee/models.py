from enum import unique
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db.models.deletion import CASCADE

# Create your models here.

class Employees(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    owner_id= models.ForeignKey('owner.Owner', to_field='business_name', on_delete = models.CASCADE)
    labor_code=ForeignKey('owner.EmployeeRoles', to_field='labor_code', on_delete = models.CASCADE)
    vacation_start_date=models.DateField
    vacation_end_date=models.DateField
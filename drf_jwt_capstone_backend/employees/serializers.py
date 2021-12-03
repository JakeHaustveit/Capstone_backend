from rest_framework import serializers
from .models import Employees

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        field = ['first_name', 'last_name', 'owner_id', 'labor_code', 'vacation_start_date', 'vacation_end_date']
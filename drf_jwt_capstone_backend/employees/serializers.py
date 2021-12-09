from rest_framework import serializers
from .models import EmployeesWorkSchedule, Employees

class EmployeesSerializer(serializers.Serializer):
    class Meta:
        model = Employees
        fields = ['first_name', 'last_name', 'username', 'owner_id', 'labor_code', 'vacation_start_date', 'vacation_end_date']


class EmployeesLoginSerializer(serializers.Serializer):
    class Meta:
        model = Employees
        fields = ['username', 'owner_id', 'first_name', 'last_name' ]        


class EmployeesWorkScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeesWorkSchedule
        fields = ["employee_id", "date_worked", "start_time", "end_time"]
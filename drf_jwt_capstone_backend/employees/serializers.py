from rest_framework import serializers
from .models import EmployeesWorkSchedule, Employees

class EmployeesSerializer(serializers.Serializer):
    class Meta:
        model = Employees
        fields = ['username', 'vacation_start_date', 'vacation_end_date']

class EmployeesWorkScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeesWorkSchedule
        fields = ["username", "labor_code", "date_worked", "start_time", "end_time"]
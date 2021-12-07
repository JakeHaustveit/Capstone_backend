from rest_framework import serializers
from .models import EmployeesWorkSchedule, Employees

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['first_name', 'last_name', 'username', 'owner_id', 'labor_code', 'vacation_start_date', 'vacation_end_date']


class EmployeesWorkScheduleSerializer(serializers.Serializer):
    class Meta:
        model = EmployeesWorkSchedule
        fields = ["date_worked", "start_time", "end_time"]
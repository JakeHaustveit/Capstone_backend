from django.db import models
from rest_framework import serializers
from .models import Owners, JobList, EmployeeRoles


class OwnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owners
        fields = ['business_name', 'user', 'first_name', 'last_name']
        

class JobListSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobList
        fields = ['job_name', 'job_site', 'job_start_date', 'job_end_date', 'business_name']

class EmployeeRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRoles
        fields = ['labor_code']
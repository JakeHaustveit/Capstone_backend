from django.db import models
from rest_framework import serializers
from .models import Owner, JobList, EmployeeRoles


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        field = ['business_name', 'user', 'first_name', 'last_name']

class JobListSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobList
        fields = ['job_name', 'job_site', 'job_start_date', 'job_end_date', 'business_name']

class EmployeeRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRoles
        fields = ['labor_code']
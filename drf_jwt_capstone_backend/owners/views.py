from django.http import request
from django.http.response import Http404
from rest_framework import serializers
from rest_framework.serializers import Serializer
from .models import JobList, EmployeeRoles
from .serializers import JobListSerializer, EmployeeRolesSerializer #OwnersSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.apps import apps 



# Create your views here.

#class Index(APIView):
#
#    def index(request):
#        Employees= apps.get_model('employees.Employees')    
#        all_employees = Employees.objects.all()
#    
#    def get_Owner(self, pk):
#        try:
#            return Owners.objects.get(pk=pk) 
#        except Owners.DoesNotExist:
#            raise Http404
#
#class OwnersRegistration(APIView):
#
#    def post(self, request):
#        serializer = OwnersSerializer(data = request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status = status.HTTP_201_CREATED)
#        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class JobListRegistration(APIView):
    
    def post(self, request):
        serializer = JobListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetAllJobs(APIView):

    def get_job_list(self, name):
        try:
            return JobList.objects.filter(business_name=name)
        except JobList.DoesNotExist:
            raise Http404
    
    def get(self,request, name):
        all_jobs = self.get_job_list(name)
        serializer = JobListSerializer(all_jobs, many = True)
        return Response(serializer.data)


class JobListData(APIView):

    def get_job_list(self, business_name):
        try:
            return JobList.objects.get(business_name=business_name)
        except JobList.DoesNotExist:
            raise Http404

    def get(self, request, business_name):
        job = self.get_job_list(business_name)
        serializer = JobListSerializer(job)
        return Response(serializer.data)

    def put(self, request, name):
        job = self.get_job_list(name)
        serializer = JobListSerializer(job, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name):
        job = self.get_job_list(name)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class EmployeeRolesRegistration(APIView):

    def post(self, request):
        serializer = EmployeeRolesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class AllEmployeeRoles(APIView):

    def get(self, request):
        all_employee_roles = EmployeeRoles.objects.all()
        serializer = EmployeeRolesSerializer(all_employee_roles, many = True)
        return Response(serializer.data)



class EmployeeRolesData(APIView):

    def get_employee_roles(self, name):
        try:
            return EmployeeRoles.objects.get(name=name)
        except JobList.DoesNotExist:
            raise Http404

    def get(self, request, name):
        employee_role = self.get_employee_roles(name)
        serializer = EmployeeRolesSerializer(employee_role)
        return Response(serializer.data)
    
    def put(self, request, name):
        employee_role = self.get_employee_roles(name)
        serializer = EmployeeRolesSerializer(employee_role)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name):
        employee_role = self.get_employee_roles(name)
        employee_role.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
from functools import partial
from django.contrib.auth import get_user_model
from django.http.response import Http404
from rest_framework.serializers import Serializer
from .models import Employees, EmployeesWorkSchedule
from .serializers import EmployeesSerializer, EmployeesWorkScheduleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
User = get_user_model()




# Create your views here.
class AddEmployee(APIView):
    
    def post(self, request):
        serializer = EmployeesSerializer( data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class GetAllEmployees(APIView):

    def get(self, request):
        all_employees= Employees.objects.all()
        serializer= EmployeesSerializer(all_employees, many = True)
        return Response(serializer.data)


class EmployeeData(APIView):

    def get_employee(self, pk):
        try:
            return Employees.objects.get(pk=pk)
        except Employees.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        employee = self.get_employee(pk)
        serializer = EmployeesSerializer(employee)
        return Response(serializer.data)
    
    def put(self, request, pk):
        employee = self.get_employee(pk)
        serializer = EmployeesSerializer(employee, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = self.get_employee(pk)
        employee.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class AddEmployeeWorkSchedule(APIView):

    def post(self, request):
        serializer = EmployeesWorkScheduleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class GetEmployeeWorkSchedule(APIView):

    def get_employee(self, name):
        try:
            return EmployeesWorkSchedule.objects.filter(username=name)

        except Employees.DoesNotExist:
            raise Http404

    def get(self, request, name):
        all_employees=  self.get_employee(name)
        serializer= EmployeesWorkScheduleSerializer(all_employees, many = True)
        return Response(serializer.data)


class EditEmployeeWorkSchedule(APIView):

    def get_employee_work_schedule(self, pk):
        try:
            return EmployeesWorkSchedule.objects.get(pk=pk)
        except EmployeesWorkSchedule.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        employee = self.get_employee_work_schedule(pk)
        serializer = EmployeesWorkScheduleSerializer(employee)
        return Response(serializer.data)
    
    def put(self, request, pk):
        employee = self.get_employee_work_schedule(pk)
        serializer = EmployeesWorkScheduleSerializer(employee, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = self.get_employee_work_schedule(pk)
        employee.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
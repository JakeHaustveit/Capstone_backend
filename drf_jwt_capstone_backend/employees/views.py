from django.http.response import Http404
from rest_framework.serializers import Serializer
from .models import Employees
from .serializers import EmployeesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
class AddEmployee(APIView):
    
    def post(self, request):
        serializer = EmployeesSerializer(data = request.data)
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
        serializer = EmployeesSerializer(employee)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = self.get_employee(pk)
        employee.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


        
from django.contrib.auth import get_user_model
from django.http.response import Http404
from rest_framework.views import APIView
from .serializers import EmployeeRegistrationSerializer, RegistrationSerializer, UserSerializar
from rest_framework import generics, serializers, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db.models import Q
User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer


class EmployeeRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = EmployeeRegistrationSerializer

class UserList(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializar(user, many=True)
        return Response(serializer.data)

class OwnerList(APIView):

    def get_object(self):
        try:
            return User.objects.filter(is_staff=True)
        except User.DoesNotExist:
            raise Http404

    def get(self, request):
        user = self.get_object()
        serializer = UserSerializar(user, many=True)
        return Response(serializer.data)


class EmployeeList(APIView):

    def get_object(self, name):
        try:
            return User.objects.filter(owner_id=name)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, name):
        user = self.get_object(name)
        serializer = EmployeeRegistrationSerializer(user, many=True)
        return Response(serializer.data)                

class UserDetail(APIView):
     
    def get_object(self, name):
        try:
            return User.objects.get(username=name)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, name):
        user = self.get_object(name)
        serializer = UserSerializar(user)
        return Response(serializer.data)

    def put(self, request, name):
        user = self.get_object(name)
        serializer = UserSerializar(user, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name):
        user = self.get_object(name)
        user.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class OwnerDetails(APIView):
    
    def get_object(self, name):
        try:
            return User.objects.get(username=name)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializar(user)
        return Response(serializer.data)


class EmployeeDetails(APIView):
    
    def get_object(self, name):
        try:
            return User.objects.get(username=name)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, name):
        user = self.get_object(name)
        serializer = UserSerializar(user)
        return Response(serializer.data)

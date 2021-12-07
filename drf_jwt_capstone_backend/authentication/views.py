from django.contrib.auth import get_user_model
from django.http.response import Http404
from rest_framework.views import APIView
from .serializers import RegistrationSerializer, UserSerializar
from rest_framework import generics, serializers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer


class UserDetail(APIView):
     
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializar(user)
        return Response(serializer.data)


from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import  RegisterView, UserDetail, UserList, EmployeeRegisterView, OwnerDetails, EmployeeDetails

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/employee/', EmployeeRegisterView.as_view()),
    path('userlist/', UserList.as_view()),
    path('userdata/<str:name>/', UserDetail.as_view()),
    path('owner/<str:name>/', OwnerDetails.as_view()),
    path('employee/<str:name>/', EmployeeDetails.as_view())
    
    
]

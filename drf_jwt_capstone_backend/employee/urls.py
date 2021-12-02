from django.urls import path
from . import views

urlpatterns = [
    path('registration/employee', views.EmployeeRegistration.as_view()),
    path('employees/', views.GetAllEmployees.as_view()),
    path('employees/<int/pk>', views.EmployeeData.as_view())
]
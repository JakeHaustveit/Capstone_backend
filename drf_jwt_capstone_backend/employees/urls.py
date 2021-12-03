from django.urls import path
from . import views


app_name = "employees"
urlpatterns = [    
    path('', views.GetAllEmployees.as_view()),
    path('home/', views.AddEmployee.as_view()),
    path('employees/<int:pk>', views.EmployeeData.as_view())
]
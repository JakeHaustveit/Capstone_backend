from django.urls import path
from . import views


app_name = "employees"
urlpatterns = [    
    path('', views.GetAllEmployees.as_view()),
    path('home/', views.AddEmployee.as_view()),
    path('addwork/', views.AddEmployeeWorkSchedule.as_view()),
    path('employeedata/<int:pk>/', views.EmployeeData.as_view()),
    path('employeeworkschedule/', views.GetEmployeeWorkSchedule.as_view()),
    path('employeeworkschedule/<int:pk>/', views.EditEmployeeWorkSchedule.as_view())
    
]
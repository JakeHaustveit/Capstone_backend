from django.urls import path
from . import views



urlpatterns = [    
    path('registerjobs/', views.JobListRegistration.as_view()),
    path('addJobs/<str:name>', views.GetAllJobs.as_view()),
    path('jobs/<str:business_name>', views.JobListData.as_view()),
    path('employeeroleregistration/', views.EmployeeRolesRegistration.as_view()),
    path('employeeroles/', views.AllEmployeeRoles.as_view()),
    path('employeeroles/<int:pk>', views.EmployeeRolesData.as_view())
]
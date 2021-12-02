from django.urls import path
from . import views

urlpatterns = [
    path('registration/owner', views.OwnerRegistration.as_view()),
    path('owner/<int/pk>', views.OwnerData.as_view()),
    path('registerjobs/', views.JobListRegistration.as_view()),
    path('jobs/', views.GetAllJobs.as_view()),
    path('jobs/<int/pk>', views.JobListData.as_view()),
    path('employeeroleregistration/', views.EmployeeRolesRegistration.as_view()),
    path('employeeroles/', views.AllEmployeeRoles.as_view()),
    path('employeeroles/<int/pk>', views.EmployeeRolesData.as_view())
]
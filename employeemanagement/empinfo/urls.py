from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('departments', views.departments, name='departments'),
    path('departments/<int:id>/', views.department_detail, name='department_detail'),
    path('departments/<int:id>/edit/', views.edit_department, name='edit_department'),
    path('departments/<int:id>/delete/', views.delete_department, name='delete_department'),
    path('departments/add/', views.add_department, name='add_department'),
    path('employees', views.employees, name='employees'),
    path('employees/<int:id>/', views.employee_detail, name='employee_detail'),
    path('employees/<int:id>/edit', views.edit_employee, name='edit_employee'),
    path('employees/<int:id>/delete', views.delete_employee, name='delete_employee'),
    path('employees/add', views.add_employee, name='add_employee'),
]
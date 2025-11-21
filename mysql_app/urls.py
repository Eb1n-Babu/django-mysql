from django.urls import path, include
from rest_framework import routers

from .views import EmployeesModelView, employees_view, employees_details, EmployeesView, EmployeesDetailsView, \
    EmployeesUpdateView, EmployeesCreateView, EmployeesDeleteView, employees_create, employees_delete, employees_update, \
    employees_list, employee_details, employee_create_view, employee_update, employee_delete

router = routers.DefaultRouter()
router.register(r'employee', EmployeesModelView)

urlpatterns = [

    path('',include(router.urls)),

    path('employee/list/create/',employees_create),
    path('employee/list/',employees_view),
    path('employee/list/<int:pk>/',employees_details),
    path('employee/list/<int:pk>/update/',employees_update),
    path('employee/list/<int:pk>/delete/',employees_delete),




    path('employee/details/create/',EmployeesCreateView.as_view(),name='employee_create'),
    path('employee/details/',EmployeesView.as_view(),name='employees_list'),
    path('employee/details/<int:pk>/',EmployeesDetailsView.as_view(),name='employee_details'),
    path('employee/details/<int:pk>/update/',EmployeesUpdateView.as_view(),name='employees_update'),
    path('employee/details/<int:pk>/delete/',EmployeesDeleteView.as_view(),name='employees_delete'),

    path('employee/new/employee/',employees_list,name='employees_list'),
    path('employee/new/employee/<int:pk>/',employee_details,name='employee_details'),
    path('employee/new/employee/create/',employee_create_view,name='employees_create'),
    path('employee/new/employee/<int:pk>/update/',employee_update,name='employees_update'),
    path('employee/new/employee/<int:pk>/delete/',employee_delete,name='employees_delete'),
]

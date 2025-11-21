from django.urls import path
from .views import EmployeesModelView , employees_view , employees_details , EmployeesView ,EmployeesDetailsView , EmployeesUpdateView ,EmployeesCreateView ,EmployeesDeleteView

urlpatterns = [
    path('employee/',EmployeesModelView.as_view({'get':'list','post':'create'})),
    path('employee/<int:pk>/',EmployeesModelView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),

    path('employee/list/',employees_view),
    path('employee/list/<int:pk>/',employees_details),



    path('employee/create/',EmployeesCreateView.as_view(),name='employee_create'),
    path('employee/details/',EmployeesView.as_view(),name='employees_list'),
    path('employee/details/<int:pk>/',EmployeesDetailsView.as_view(),name='employee_details'),
    path('employee/details/<int:pk>/update/',EmployeesUpdateView.as_view(),name='employees_update'),
    path('employee/details/<int:pk>/delete/',EmployeesDeleteView.as_view(),name='employees_delete'),
]

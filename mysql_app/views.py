from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views import generic

from .forms import EmployeesForm
from .models import  Employees
from serializers import EmployeesSerializer


class EmployeesModelView(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

@api_view(['GET'])
def employees_view(request):
    employees = Employees.objects.all()
    serializer = EmployeesSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def employees_details(request,pk):
    employee = Employees.objects.get(pk=pk)
    serializer = EmployeesSerializer(employee)
    return Response(serializer.data)

@api_view(['POST'])
def employees_create(request):
    serializer = EmployeesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def employees_update(request,pk):
    employee = Employees.objects.get(pk=pk)
    serializer = EmployeesSerializer(employee, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def employees_delete(request,pk):
    employee = Employees.objects.get(pk=pk)
    employee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class  EmployeesView(generic.ListView):
    queryset = Employees.objects.all()
    context_object_name = 'employees'
    template_name = 'employees_list.html'

class EmployeesDetailsView(generic.DetailView):
    queryset = Employees.objects.all()
    context_object_name = 'employee'
    template_name = 'employee_details.html'

class EmployeesUpdateView(generic.UpdateView):
    queryset = Employees.objects.all()
    form_class = EmployeesForm
    template_name = 'employees_update.html'
    success_url = '/employee/details/'

class EmployeesCreateView(generic.CreateView):
    queryset = Employees.objects.all()
    form_class = EmployeesForm
    template_name = 'employees_create.html'
    success_url = '/employee/details/'

class EmployeesDeleteView(generic.DeleteView):
    queryset = Employees.objects.all()
    context_object_name = 'employee'
    template_name = 'employees_delete.html'
    success_url = '/employee/details/'

def employees_list(request):
    employees = Employees.objects.all()
    return render(request,'employees_list.html',{'employees':employees})

def employee_details(request,pk):
    employee = Employees.objects.get(pk=pk)
    return render(request,'employee_details.html',{'employee':employee})

def employee_create_view(request):
    if request.method == 'POST':
        form = EmployeesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("success")
        else:
            return HttpResponse("error")
    else:
        form = EmployeesForm()
        return render(request,'employees_create.html',{'form':form})

def employee_delete(request,pk):
    employee = Employees.objects.get(pk=pk)
    employee.delete()
    return HttpResponse("success")

def employee_update(request,pk):
    if request.method == 'POST':
        form = EmployeesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("success")
        else:
            return HttpResponse("error")

    else:
        form = EmployeesForm()
        return render(request,'employees_update.html',{'form':form})

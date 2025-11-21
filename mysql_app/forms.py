from django import forms

from mysql_app.models import Employees


class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'

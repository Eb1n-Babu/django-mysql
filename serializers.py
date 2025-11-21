from rest_framework import serializers
from mysql_app.models import Employees


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'
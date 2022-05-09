from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from testapp.models import Employee
from testapp.serializer import EmployeeSerializer


# Create your views here.
class EmployeeViewSet(ModelViewSet):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()

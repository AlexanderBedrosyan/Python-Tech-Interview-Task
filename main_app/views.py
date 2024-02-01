from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

from main_app.models import Employee
# Create your views here.
import jinja2

# djangorestframework
from rest_framework import viewsets, generics
from .serializer import EmployeeModelSerializer
from django.shortcuts import render, redirect
from .models import Employee
from django.http import HttpResponse


# djangorestframework
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer


class EmployeeUpdateView(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer


def front_page(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mobile = request.POST.get('mobile')
        start_date = request.POST.get('start_date')
        position = request.POST.get('position')
        salary = request.POST.get('salary')
        employee_id = request.POST.get('employee_id')

        Employee.objects.create(
            first_name=first_name,
            last_name=last_name,
            mobile=mobile,
            start_date=start_date,
            position=position,
            salary=salary,
            employee_id=employee_id
        )

        return HttpResponse("Employee added successfully!")

    employees = Employee.objects.all()
    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
    jinja_var = {
        'employees': employees,
        'title': 'Employees Information',
    }
    return render(request, 'front_page.html', jinja_var)
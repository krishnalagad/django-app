from django.http import HttpResponse
from django.shortcuts import render

from emp.models import Employee

def starter(request):
    emps = Employee.objects.all()
    return render(request, 'emp/home.html', {
        'emps': emps,
    })
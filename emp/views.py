from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Employee

# Create your views here.
def employee_home(request):

    emps = Employee.objects.all()
    # return HttpResponse("Employee Home Page")
    return render(request, "emp/home.html", {
        'emps': emps,
    })

def add_emp(request):
    if request.method == 'POST':

        # data fetch 
        emp_name = request.POST.get('emp_name')
        emp_id = request.POST.get('emp_id')
        emp_phone = request.POST.get('emp_phone')
        emp_address = request.POST.get('emp_address')
        emp_working = request.POST.get('emp_working')
        emp_department = request.POST.get('emp_department')

        # validations here

        # create model object and set the data to
        e = Employee()
        e.name = emp_name
        e.emp_id = emp_id
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department
        if emp_working is None:
            e.working = False
        else:
            e.working = True

        # save the object
        e.save()

        # prepare msg
        return redirect("/employee/home/")
    return render(request, "emp/add_emp.html", {})

def delete_emp(request, emp_id):
    emp = Employee.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/employee/home/")

def update_emp(request, emp_id):
    emp = Employee.objects.get(pk=emp_id)
    return render(request, "emp/update_emp.html",{
        'emp':emp
    })

def do_update_emp(request, emp_id):
    if request.method == 'POST':
        emp_name = request.POST.get('emp_name')
        emp_id_temp = request.POST.get('emp_id')
        emp_phone = request.POST.get('emp_phone')
        emp_address = request.POST.get('emp_address')
        emp_working = request.POST.get('emp_working')
        emp_department = request.POST.get('emp_department')

        e = Employee.objects.get(pk=emp_id)
        e.name = emp_name
        e.emp_id = emp_id_temp
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department
        if emp_working is None:
            e.working = False
        else:
            e.working = True

        e.save()
        return redirect("/employee/home/")

    return render(request, "emp/update_emp.html",{
        'emp':e
    })
    
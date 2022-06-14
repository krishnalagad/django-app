from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("home/", employee_home),
    path("add-emp/", add_emp),
    path("delete-emp/<int:emp_id>", delete_emp),
    path("update-emp/<int:emp_id>", update_emp),
    path("do_update_emp/<int:emp_id>", do_update_emp),
]

# esalary/admin.py
from django.contrib import admin
from .models import Employee, Salary, SalarySchedule

admin.site.register(Employee)
admin.site.register(Salary)
admin.site.register(SalarySchedule)

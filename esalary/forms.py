from django import forms
from .models import Employee, Salary, SalarySchedule

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name']

class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = ['employee', 'basic_salary', 'bonuses', 'deductions', 'schedule']

class SalaryScheduleForm(forms.ModelForm):
    class Meta:
        model = SalarySchedule
        fields = ['name', 'payment_day', 'payment_frequency']

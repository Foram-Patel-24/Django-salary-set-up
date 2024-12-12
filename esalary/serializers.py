from rest_framework import serializers
from .models import Salary, Employee, SalarySchedule

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name']  

class SalarySerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer() 
    total_salary = serializers.SerializerMethodField()  

    class Meta:
        model = Salary
        fields = ['employee', 'basic_salary', 'bonuses', 'deductions', 'schedule', 'total_salary']

    def get_total_salary(self, obj):
        return obj.total_salary() 
    
    
class SalaryScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalarySchedule
        fields = ['name', 'payment_day', 'payment_frequency']


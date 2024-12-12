from django.db import models

class SalarySchedule(models.Model):
    name = models.CharField(max_length=100)
    payment_day = models.IntegerField(help_text="Day of the month the salary is paid")
    payment_frequency = models.CharField(
        max_length=20,
        choices=[('Monthly', 'Monthly'), ('Weekly', 'Weekly'), ('Bi-Weekly', 'Bi-Weekly')],
        default='Monthly',
    )

    def __str__(self):
        return f"{self.name} ({self.payment_frequency})"


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonuses = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    schedule = models.ForeignKey(SalarySchedule, on_delete=models.CASCADE)

    def total_salary(self):
        return self.basic_salary + (self.bonuses or 0) - (self.deductions or 0)

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} Salary"

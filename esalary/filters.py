from django_filters import rest_framework as filters
from .models import SalarySchedule

class SalaryScheduleFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')  # Partial match for name

    class Meta:
        model = SalarySchedule
        fields = ['name', 'payment_day', 'payment_frequency']

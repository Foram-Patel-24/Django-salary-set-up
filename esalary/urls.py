from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SalaryViewSet , EmployeeViewSet , SalaryScheduleViewSet

router = DefaultRouter()
router.register(r'salaries', SalaryViewSet, basename='salary')
router.register(r'SalarySchedule', SalaryScheduleViewSet, basename='SalarySchedule')
router.register(r'Employees', EmployeeViewSet, basename='Employee')

urlpatterns = [
    path('api/', include(router.urls)),
]
    
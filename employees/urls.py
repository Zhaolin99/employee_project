from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, DepartmentViewSet, employees_per_department, monthly_attendance_overview

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'departments', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('charts/employees-per-department/', employees_per_department, name='employees_per_department'),
    path('charts/monthly-attendance-overview/', monthly_attendance_overview, name='monthly_attendance_overview'),
]

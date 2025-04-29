from rest_framework import viewsets, filters, permissions
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from .permissions import IsAdmin, IsHR, IsEmployee

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['department', 'date_joined']
    search_fields = ['name', 'email']
    ordering_fields = ['name', 'date_joined', 'id']
    ordering = ['id']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated, (IsAdmin | IsHR)]
        else:
            permission_classes = [permissions.IsAuthenticated, (IsAdmin | IsHR | IsEmployee)]
        return [permission() for permission in permission_classes]



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdmin | IsHR]
        else:
            permission_classes = [IsAdmin | IsHR | IsEmployee]
        return [permission() for permission in permission_classes]

# Visulization
def charts_view(request):
    return render(request, 'charts.html')

from rest_framework.decorators import api_view
from rest_framework.response import Response
from attendance.models import Attendance
from django.db.models import Count
from django.db.models.functions import TruncMonth
import calendar

# API for Employees per Department
@api_view(['GET'])
def employees_per_department(request):
    data = Employee.objects.values('department__name').annotate(count=Count('id'))
    result = {item['department__name']: item['count'] for item in data}
    return Response(result)

# API for Monthly Attendance Overview
@api_view(['GET'])
def monthly_attendance_overview(request):
    data = Attendance.objects.annotate(month=TruncMonth('date')).values('month').annotate(count=Count('id')).order_by('month')
    result = {calendar.month_name[item['month'].month]: item['count'] for item in data if item['month']}
    return Response(result)



from rest_framework import viewsets, permissions
from .models import Attendance, Performance
from .serializers import AttendanceSerializer, PerformanceSerializer
from employees.permissions import IsAdmin, IsHR, IsEmployee

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), (IsAdmin() or IsHR())]
        return [permissions.IsAuthenticated()]


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), (IsAdmin() or IsHR())]
        return [permissions.IsAuthenticated()]

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from employees.views import charts_view
from django.http import HttpResponse

swagger_schema_view = get_schema_view(
    openapi.Info(
        title="Employee Management API",
        default_version='v1',
        description="API documentation for Employee Management System",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[],
)


schema_view = get_schema_view(
    openapi.Info(
        title="Employee Management API",
        default_version='v1',
        description="API documentation for Employee, Department, Attendance, Performance models",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="your-email@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[], # Allow Swagger UI Authorization
)

def home(request):
    return HttpResponse("Welcome to the Employee Management System")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('employees.urls')),
    path('api/', include('attendance.urls')),
    # JWT Auth endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Swagger Document
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('charts/', charts_view, name='charts'),
]

"""
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0NjQxNzE4MywiaWF0IjoxNzQ1ODEyMzgzLCJqdGkiOiJkMjFhOGM2MWM5Nzk0OTUzODgyOGI1NWQ1NzQ4MzNhMyIsInVzZXJfaWQiOjF9.D0t4Fq7q9g3PP4NHJWL2_mb2tDWL5fPAu6i7Cpdrx-s",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1ODEyNjgzLCJpYXQiOjE3NDU4MTIzODMsImp0aSI6ImI3NTQ0ODY2YTg2MTQwMzdhYTMwYjgzZGYyNzY5NTI1IiwidXNlcl9pZCI6MX0.-WXUsl2bT_SfBJfONrhTU4bKRFWA0NhN2Z0To4sTwD8"
}
"""

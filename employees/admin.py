from django.contrib import admin
from .models import Department, Employee, CustomUser
from django.contrib.auth.admin import UserAdmin

admin.site.register(Department)
admin.site.register(Employee)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'role', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Role Info', {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Role Info', {'fields': ('role',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
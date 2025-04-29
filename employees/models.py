from django.db import models
from django.contrib.auth.models import AbstractUser

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    address = models.TextField()
    date_joined = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('HR', 'HR'),
        ('Employee', 'Employee'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Employee')

    def __str__(self):
        return f"{self.username} ({self.role})"
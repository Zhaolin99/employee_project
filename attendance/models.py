from django.db import models
from employees.models import Employee  # FK reference

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.employee.name} - {self.date}"

class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_date = models.DateField()

    def __str__(self):
        return f"{self.employee.name} - {self.rating}"

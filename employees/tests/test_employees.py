from django.test import TestCase
from rest_framework.test import APIClient
from employees.models import CustomUser, Department, Employee
from rest_framework import status
from datetime import date

class EmployeeTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.department = Department.objects.create(name='Engineering')

        self.hr_user = CustomUser.objects.create_user(
            username='hruser',
            password='hrpass',
            role='HR'
        )

        self.employee_user = CustomUser.objects.create_user(
            username='employee1',
            password='emppass',
            role='Employee'
        )

        self.employee_record = Employee.objects.create(
            name='John Doe',
            email='john@example.com',
            phone='1234567890',
            address='123 Test St',
            department=self.department,
            date_joined=date.today()
        )

    def get_token(self, username, password):
        res = self.client.post('/api/token/', {'username': username, 'password': password})
        return res.data['access']

    def test_hr_can_view_employees(self):
        token = self.get_token('hruser', 'hrpass')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        res = self.client.get('/api/employees/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(res.data.get('results', [])), 1)

    def test_employee_cannot_create_employee(self):
        token = self.get_token('employee1', 'emppass')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        res = self.client.post('/api/employees/', {
            'name': 'Fake Emp',
            'email': 'fake@example.com',
            'phone': '9999999999',
            'address': 'Hidden',
            'date_joined': '2024-01-01',
            'department': self.department.id
        })

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

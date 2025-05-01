from django.test import TestCase
from rest_framework.test import APIClient
from employees.models import CustomUser
from rest_framework import status

class AuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = CustomUser.objects.create_user(
            username='adminuser',
            password='adminpass',
            role='Admin'
        )

    def test_token_generation(self):
        response = self.client.post('/api/token/', {
            'username': 'adminuser',
            'password': 'adminpass'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_invalid_login(self):
        response = self.client.post('/api/token/', {
            'username': 'adminuser',
            'password': 'wrongpass'
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

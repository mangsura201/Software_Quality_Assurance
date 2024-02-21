"""User Login Unit Testing"""
from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .views import custom_login

class CustomLoginViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.admin_user = User.objects.create_superuser(username='admin', email='admin@example.com', password='adminpassword')

    def test_authenticated_user_superuser(self):
        request = self.factory.get('/')
        request.user = self.admin_user
        response = custom_login(request)
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertEqual(response.url, '/admin_dashboard/')  # Should redirect to admin dashboard

    def test_authenticated_user_non_superuser(self):
        request = self.factory.get('/')
        request.user = self.user
        response = custom_login(request)
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertEqual(response.url, '/customer_dashboard/')  # Should redirect to customer dashboard

    def test_unauthenticated_user(self):
        request = self.factory.get('/')
        request.user = AnonymousUser()  # Simulate unauthenticated user
        response = custom_login(request)
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertEqual(response.url, '/login/')  # Should redirect to the login page

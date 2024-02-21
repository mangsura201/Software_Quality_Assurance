from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import CustomerCreationForm
from .models import UserProfile


"""Unit Testing for Add Customer"""
class AddCustomerViewTest(TestCase):
    """
    Test case for the add_customer view.

    Methods:
    --------
    setUp(self)
        Sets up the necessary data for testing.
    test_add_customer_view(self)
        Tests the behavior of the add_customer view for GET requests.
    test_add_customer_post(self)
        Tests the behavior of the add_customer view for POST requests.
    """
    def setUp(self):
        """
        Set up the necessary data for testing.

        Creates a test user and logs in with the user credentials.
        """
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')

    def test_add_customer_view(self):
        """
        Test the behavior of the add_customer view for GET requests.

        Checks if the view returns a status code of 200, uses the correct template,
        and passes a CustomerCreationForm instance to the template context.
        """
        url = reverse('add_customer')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_customer.html')
        self.assertIsInstance(response.context['form'], CustomerCreationForm)

    def test_add_customer_post(self):
        """
        Test the behavior of the add_customer view for POST requests.

        Checks if the view redirects to the admin dashboard upon successful form submission,
        and verifies if the user and user profile are created in the database.
        """
        url = reverse('add_customer')
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'bank_account_no': '1234567890',
            'phone_no': '1234567890'
        }
        response = self.client.post(url, data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('admin_dashboard'))

        # Check if the user and user profile are created
        self.assertTrue(User.objects.filter(username='johndoe').exists())
        self.assertTrue(UserProfile.objects.filter(user__username='johndoe').exists())





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

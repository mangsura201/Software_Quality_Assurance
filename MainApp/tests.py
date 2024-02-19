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



"""See all customer unit test"""
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import UserProfile
from .views import see_all_customers

class ViewTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a test customer
        self.customer = UserProfile.objects.create(user=self.user, bank_account_no='1234567890', phone_no='9876543210', balance=100.00)

    def test_see_all_customers(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        # Access the see_all_customers view
        response = self.client.get('/see_all_customers/')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the 'see_all_customers.html' template is used
        self.assertTemplateUsed(response, 'see_all_customers.html')

        # Check if the 'customers' variable is present in the context
        self.assertIn('customers', response.context)

        # Check if the rendered HTML contains the customer's information
        self.assertContains(response, self.customer.bank_account_no)
        self.assertContains(response, self.customer.phone_no)
        self.assertContains(response, str(self.customer.balance))

    def create_request(self):
        # Create a mock request object
        request = RequestFactory().get('/see_all_customers/')
        request.user = self.user
        return request


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

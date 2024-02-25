
"""Unit testing See all customer"""
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
        self.assertTemplateUsed(response, 'Sayma/see_all_customers.html')

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

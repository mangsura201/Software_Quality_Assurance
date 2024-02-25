from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile
from .customer_dashboard_views import customer_dashboard

class CustomerDashboardTestCase(TestCase):
    def setUp(self):
        # Create a sample user profile for testing
        self.user = User.objects.create_user(username='testuser', password='password')
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            bank_account_no='1234567890',
            phone_no='1234567890',
            balance=1000
        )

    def test_customer_dashboard(self):
        # Create a test client
        client = Client()
        
        # Log in the user
        client.login(username='testuser', password='password')

        # Make a GET request to the view
        response = client.get(reverse('customer_dashboard'))

        # Check if the response is successful
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is being used
        self.assertTemplateUsed(response, 'Sayma/customer_dashboard.html')

        # Check if the user details are present in the context
        self.assertEqual(response.context['user'], self.user)
from .see_all_customer_views import see_all_customers

"""Unit testing for See all customer"""
from django.test import TestCase, Client
from django.urls import reverse
from .models import UserProfile
from django.contrib.auth.models import User

class SeeAllCustomersTestCase(TestCase):
    def setUp(self):
        # Create sample user profiles for testing
        self.user1 = User.objects.create_user(username='user1', password='password1')
        self.profile1 = UserProfile.objects.create(user=self.user1, bank_account_no='123', phone_no='1234567890', balance=100)
        
        self.user2 = User.objects.create_user(username='user2', password='password2')
        self.profile2 = UserProfile.objects.create(user=self.user2, bank_account_no='456', phone_no='4567890123', balance=200)

    def test_see_all_customers(self):
        # Create a test client
        client = Client()
        
        # Make a GET request to the view
        response = client.get(reverse('see_all_customers'))
        
        # Check if the response is successful
        self.assertEqual(response.status_code, 200)
        
        # Check if the correct template is being used
        self.assertTemplateUsed(response, 'Sayma/see_all_customers.html')
        
        # Check if the customers are present in the context
        customers = response.context['customers']
        self.assertEqual(customers.count(), 2)  # Ensure all customers are retrieved
        
        # Check if the retrieved customers match the expected data
        self.assertIn(self.profile1, customers)
        self.assertIn(self.profile2, customers)
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from MainApp.add_customer_views import *
from MainApp.add_money_views import *
from MainApp.all_transaction_views import *
from MainApp.see_all_customer_views import *
from MainApp.chat_system_views import *
from MainApp.login_logout_views import *
from MainApp.money_transfer_views import *
from MainApp.profile_update_views import *
from MainApp.views import *
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from MainApp.models import UserProfile, Transaction, Message
from MainApp.forms import *

class ViewsTestCase(TestCase):
    def setUp(self):
        # Create a test user for authentication
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.user_profile = UserProfile.objects.create(user=self.user, bank_account_no='123456789', phone_no='1234567890')

    def test_customer_dashboard_view(self):
        # Test customer_dashboard view
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('customer_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Sayma/customer_dashboard.html')

    def test_money_transfer_view(self):
        # Test money_transfer view
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('money_transfer'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shifat/money_transfer.html')


    def test_admin_dashboard(self):
        # Test admin_dashboard view
        response = self.client.get(reverse('admin_dashboard'))
        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response

    def test_see_all_customers(self):
        # Test see_all_customers view
        response = self.client.get(reverse('see_all_customers'))
        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response

    def test_add_customer(self):
        # Test add_customer view
        response = self.client.get(reverse('add_customer'))
        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response

    def test_delete_customer(self):
        # Test delete_customer view
        response = self.client.get(reverse('delete_customer', args=[self.user_profile.id]))
        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response

    def test_add_money(self):
        # Test add_money view
        response = self.client.get(reverse('add_money', args=[self.user_profile.id]))
        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response

    def test_customer_transaction(self):
        # Test customer_transaction view
        response = self.client.get(reverse('transaction_details', args=[self.user_profile.id]))
        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response

    def test_see_all_transactions(self):
        # Test see_all_transactions view
        response = self.client.get(reverse('see_all_transactions'))
        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response

    def test_customer_dashboard(self):
        # Test customer_dashboard view
        response = self.client.get(reverse('customer_dashboard'))
        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response

    def test_update_profile(self):
        # Test update_profile view
        response = self.client.get(reverse('update_customer', args=[self.user_profile.id]))
        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response

    def test_money_transfer(self):
        # Test money_transfer view
        response = self.client.get(reverse('money_transfer'))
        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response

    def test_chat_with_admin(self):
        # Test chat_with_admin view
        response = self.client.get(reverse('chat_with_admin'))
        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response

    def test_send_message(self):
        # Test send_message view
        response = self.client.get(reverse('send_message', args=[self.user.username]))
        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response

    def test_inbox(self):
        # Test inbox view
        response = self.client.get(reverse('inbox'))
        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response

    def test_sentbox(self):
        # Test sentbox view
        response = self.client.get(reverse('sentbox'))
        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response

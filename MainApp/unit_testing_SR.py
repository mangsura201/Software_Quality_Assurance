
""" Unit Testing for money transfer  """
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile, Transaction
from django.test import TestCase, Client


class MoneyTransferViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='sender', email='sender@example.com', password='password')
        self.user_profile = UserProfile.objects.create(user=self.user, bank_account_no='1234567890', phone_no='1234567890', balance=1000)
        self.receiver_user = User.objects.create_user(username='receiver', email='receiver@example.com', password='password')
        self.receiver_user_profile = UserProfile.objects.create(user=self.receiver_user, bank_account_no='0987654321', phone_no='0987654321', balance=0)

    def test_money_transfer_successful(self):
        self.client.login(username='sender', password='password')
        data = {
            'receiver_username': 'receiver',
            'receiver_email': 'receiver@example.com',
            'receiver_bank_account_no': '0987654321',
            'amount': 100,
            'sender_bank_account_no': '1234567890',
            'sender_username': 'sender',
            'password': 'password'
        }
        response = self.client.post(reverse('money_transfer'), data)
        self.assertEqual(response.status_code, 302)  # Redirects to customer_dashboard
        sender = UserProfile.objects.get(user=self.user)
        receiver = UserProfile.objects.get(user=self.receiver_user)
        self.assertEqual(sender.balance, 900)
        self.assertEqual(receiver.balance, 100)

    def test_insufficient_balance(self):
        self.client.login(username='sender', password='password')
        data = {
            'receiver_username': 'receiver',
            'receiver_email': 'receiver@example.com',
            'receiver_bank_account_no': '0987654321',
            'amount': 2000,  # Exceeding sender's balance
            'sender_bank_account_no': '1234567890',
            'sender_username': 'sender',
            'password': 'password'
        }
        response = self.client.post(reverse('money_transfer'), data)
        self.assertIsInstance(response, HttpResponseRedirect)  # Check if redirect happened
        self.assertEqual(response.url, '/money_transfer/')  # Ensure redirected to money_transfer page

    def test_invalid_sender_credentials(self):
        self.client.login(username='sender', password='password')
        data = {
            'receiver_username': 'receiver',
            'receiver_email': 'receiver@example.com',
            'receiver_bank_account_no': '0987654321',
            'amount': 100,
            'sender_bank_account_no': 'invalid',  # Invalid sender bank account number
            'sender_username': 'sender',
            'password': 'password'
        }
        response = self.client.post(reverse('money_transfer'), data)
        self.assertIsInstance(response, HttpResponseRedirect)  # Check if redirect happened
        self.assertEqual(response.url, '/money_transfer/')  # Ensure redirected to money_transfer page"""


""" Unit Testing for see transaction details and customer transaction """
class CustomerTransactionViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.user_profile = UserProfile.objects.create(user=self.user, bank_account_no='1234567890', phone_no='1234567890', balance=1000)
        self.transaction = Transaction.objects.create(sender_account_no='1234567890', receiver_account_no='0987654321', amount=100, transaction_id='12345678')

    def test_customer_transaction_view(self):
        self.client.force_login(self.user)
        url = reverse('customer_transaction', kwargs={'customer_id': self.user_profile.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer_transaction.html')

class SeeAllTransactionViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = User.objects.create_superuser(username='admin', email='admin@example.com', password='adminpassword')
        self.transaction = Transaction.objects.create(sender_account_no='1234567890', receiver_account_no='0987654321', amount=100, transaction_id='12345678')

    def test_see_all_transaction_view_superuser(self):
        self.client.force_login(self.admin_user)
        url = reverse('see_all_transaction')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'see_all_transaction.html')

    def test_see_all_transaction_view_non_superuser(self):
        non_admin_user = User.objects.create_user(username='user', email='user@example.com', password='userpassword')
        self.client.force_login(non_admin_user)
        url = reverse('see_all_transaction')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Assuming it renders a template even for non-superusers
        self.assertTemplateUsed(response, 'admin_dashboard.html')
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

from django.test import TestCase
from .forms import MoneyTransferForm
from .models import UserProfile
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

class MoneyTransferTestCase(TestCase):
    def setUp(self):
        # Create a user using Django's built-in User model
        self.sender_user = User.objects.create_user(username='sender', password='password')
        
        # Create a user profile associated with the created user
        self.sender = UserProfile.objects.create(
            user=self.sender_user,
            bank_account_no='1234567890',
            phone_no='1234567890',  # Adjust phone number as needed
            balance=1000  # Adjust initial balance as needed
        )

    def test_valid_transfer(self):
        form_data = {
            'receiver_username': 'receiver',
            'receiver_email': 'receiver@example.com',
            'receiver_bank_account_no': '1234567890',
            'amount': 500,  # an amount within sender's balance
            'sender_bank_account_no': self.sender.bank_account_no,
            'sender_username': self.sender.user.username,
            'password': 'password',
        }
        form = MoneyTransferForm(data=form_data)
        self.assertTrue(form.is_valid())  # Ensure form is valid

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
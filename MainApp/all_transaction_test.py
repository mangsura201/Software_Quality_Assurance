from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client
from .models import Transaction

class SeeAllTransactionsTestCase(TestCase):
    def setUp(self):
        # Create a superuser
        self.admin_user = User.objects.create_superuser(
            username='admin',
            password='adminpassword',
            email='admin@example.com'
        )

        # Create a regular user
        self.regular_user = User.objects.create_user(
            username='user',
            password='userpassword',
            email='user@example.com'
        )

        # Create a transaction
        self.transaction = Transaction.objects.create(
            amount=100,
            description='Test Transaction',
            date='2022-01-01'
        )

    def test_admin_can_see_all_transactions(self):
        client = Client()
        client.force_login(self.admin_user)

        response = client.get(reverse('see_all_transactions'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'see_all_transaction.html')
        self.assertIn('all_transactions', response.context)
        transactions = response.context['all_transactions']
        self.assertEqual(transactions.count(), 1)
        self.assertEqual(transactions[0], self.transaction)

    def test_regular_user_redirected(self):
        client = Client()
        client.force_login(self.regular_user)

        response = client.get(reverse('see_all_transactions'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_dashboard.html')
        self.assertIn('message', response.context)
        message = response.context['message']
        self.assertEqual(message, 'You are not authorized to view this page')

    def test_unauthenticated_user_redirected_to_login(self):
        client = Client()

        response = client.get(reverse('see_all_transactions'))
        self.assertRedirects(response, '/accounts/login/?next=/see_all_transactions/')

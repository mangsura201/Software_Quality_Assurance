from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile, Transaction

class AddMoneyViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.userprofile = UserProfile.objects.create(user=cls.user, bank_account_no='1234567890', balance=100)

    def test_add_money_view(self):
        # Log in the user
        self.client.login(username='testuser', password='12345')

        # Define the URL and data for the POST request
        url = reverse('add_money', args=[self.userprofile.id])
        data = {'balance': 50}

        # Make the POST request
        response = self.client.post(url, data)

        # Check if the balance is updated
        self.userprofile.refresh_from_db()
        self.assertEqual(self.userprofile.balance, 150)

        # Check if a transaction record is created
        transactions_count = Transaction.objects.count()
        self.assertEqual(transactions_count, 1)

        # Check if the transaction record corresponds to the correct user
        transaction = Transaction.objects.first()
        self.assertEqual(transaction.receiver_account_no, self.userprofile.bank_account_no)
        self.assertEqual(transaction.amount, 50)

        
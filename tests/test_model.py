from django.test import TestCase
from MainApp.models import UserProfile, Transaction
from django.contrib.auth.models import User


class UserProfileTestCase(TestCase):
    def test_user_profile_creation(self):
        """
        Test user profile creation.

        This test case checks whether a user profile can be created successfully.
        """
        
        user = User.objects.create(username='mangsurakabir')
        profile = UserProfile.objects.create(user=user, bank_account_no='1234567890', balance=1000)
        self.assertIsNotNone(profile)

class TransactionTestCase(TestCase):
    def test_transaction_creation(self):
        """
        Test transaction creation.

        This test case verifies the creation of a transaction.
        """
        
        transaction = Transaction.objects.create(
            sender_account_no='1234567890',
            receiver_account_no='0987654321',
            amount=500,
            transaction_id='12345678'
        )
        self.assertIsNotNone(transaction)

    def test_transaction_id_generation(self):
        """
        Test transaction ID generation.

        This test case ensures that a transaction ID is generated upon transaction creation.
        """
        
        transaction = Transaction.objects.create(
            sender_account_no='1234567890',
            receiver_account_no='0987654321',
            amount=500
        )
        self.assertIsNotNone(transaction.transaction_id)

   
        
# In myapp/tests/test_models.py
from django.test import TestCase
from MainApp.models import UserProfile, Transaction, Message
from django.contrib.auth.models import User

class ModelTestCase(TestCase):
    def setUp(self):
        # Create test data for UserProfile
        self.user = User.objects.create(username='testuser')
        self.profile = UserProfile.objects.create(
            user=self.user,
            bank_account_no='1234567890',
            phone_no='1234567890',
            balance=1000
        )

    def test_user_profile_creation(self):
        # Test UserProfile creation
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.bank_account_no, '1234567890')
        self.assertEqual(self.profile.phone_no, '1234567890')
        self.assertEqual(self.profile.balance, 1000)

    def test_transaction_creation(self):
        # Test Transaction creation
        transaction = Transaction.objects.create(
            sender_account_no='sender123',
            receiver_account_no='receiver456',
            amount=500
        )
        self.assertIsNotNone(transaction.transaction_id)
        self.assertEqual(transaction.sender_account_no, 'sender123')
        self.assertEqual(transaction.receiver_account_no, 'receiver456')
        self.assertEqual(transaction.amount, 500)

    def test_message_creation(self):
        # Test Message creation
        sender = User.objects.create(username='sender')
        receiver = User.objects.create(username='receiver')
        message = Message.objects.create(
            sender=sender,
            receiver=receiver,
            subject='Test Subject',
            body='Test Body'
        )
        self.assertEqual(message.sender, sender)
        self.assertEqual(message.receiver, receiver)
        self.assertEqual(message.subject, 'Test Subject')
        self.assertEqual(message.body, 'Test Body')

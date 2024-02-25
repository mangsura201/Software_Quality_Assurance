from django.test import TestCase
from django.contrib.auth.models import User
from MainApp.models import UserProfile, Transaction, Message

class UserProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user', email='test@example.com')
        self.profile = UserProfile.objects.create(
            user=self.user,
            bank_account_no='1234567890',
            phone_no='1234567890',
            balance=1000
        )

    def test_user_profile_creation(self):
        self.assertEqual(self.profile.user.username, 'test_user')
        self.assertEqual(self.profile.bank_account_no, '1234567890')
        self.assertEqual(self.profile.phone_no, '1234567890')
        self.assertEqual(self.profile.balance, 1000)

class TransactionTestCase(TestCase):
    def test_transaction_creation(self):
        # Create a sample transaction
        transaction = Transaction.objects.create(
            sender_account_no='sender123',
            receiver_account_no='receiver456',
            amount=500
        )
        # Verify transaction details
        self.assertEqual(transaction.sender_account_no, 'sender123')
        self.assertEqual(transaction.receiver_account_no, 'receiver456')
        self.assertEqual(transaction.amount, 500)

class MessageTestCase(TestCase):
    def test_message_creation(self):
        # Create a sample message
        sender_user = User.objects.create(username='sender', email='sender@example.com')
        receiver_user = User.objects.create(username='receiver', email='receiver@example.com')
        message = Message.objects.create(
            sender=sender_user,
            receiver=receiver_user,
            subject='Test Subject',
            body='Test Body'
        )
        # Verify message details
        self.assertEqual(message.sender.username, 'sender')
        self.assertEqual(message.receiver.username, 'receiver')
        self.assertEqual(message.subject, 'Test Subject')
        self.assertEqual(message.body, 'Test Body')

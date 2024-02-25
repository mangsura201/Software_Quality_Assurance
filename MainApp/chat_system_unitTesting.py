from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message
from .forms import MessageForm

class MessageModelTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')
        self.message = Message.objects.create(sender=self.user1, receiver=self.user2, subject='Test Subject', body='Test Body')

    def test_message_creation(self):
        self.assertEqual(self.message.sender, self.user1)
        self.assertEqual(self.message.receiver, self.user2)
        self.assertEqual(self.message.subject, 'Test Subject')
        self.assertEqual(self.message.body, 'Test Body')

class MessageViewsTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')

    def test_send_message_view(self):
        self.client.login(username='user1', password='password')
        response = self.client.post('/send_message/user2/', {'receiver': 2, 'subject': 'Test Subject', 'body': 'Test Body'})
        self.assertEqual(response.status_code, 302)  # Redirects to sentbox upon successful sending

    def test_inbox_view(self):
        self.client.login(username='user2', password='password')
        response = self.client.get('/inbox/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['messages']), 0)  # No messages in the inbox

    def test_sentbox_view(self):
        self.client.login(username='user1', password='password')
        response = self.client.get('/sentbox/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['messages']), 0)  # No sent messages yet


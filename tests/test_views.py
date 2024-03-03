"""from django.test import TestCase, Client
from django.contrib.auth.models import User
from MainApp.models import UserProfile, Transaction
from MainApp.add_money_views import add_money  # Assuming this is the actual view function


class AddMoneyViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = UserProfile.objects.create(user=self.user, balance=100)

    def test_add_money_get(self):
        response = self.client.get(f'/add_money/{self.profile.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mangsura/add_money.html')

    def test_add_money_post_valid(self):
        data = {'balance': 50}
        response = self.client.post(f'/add_money/{self.profile.id}/', data)
        self.assertEqual(response.status_code, 302)  # Redirected

        # Assert changes in model and transaction creation
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.balance, 150)
        transaction = Transaction.objects.get(receiver_account_no=self.profile.bank_account_no)
        self.assertEqual(transaction.amount, 50)

    def test_add_money_post_invalid(self):
        data = {'balance': -100}  # Invalid negative value
        response = self.client.post(f'/add_money/{self.profile.id}/', data)
        self.assertEqual(response.status_code, 200)  # Form is rendered again
        self.assertContains(response, 'Ensure this value is greater than or equal to 0.')"""

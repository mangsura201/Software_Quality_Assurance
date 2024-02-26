from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from MainApp.forms import ProfileUpdateForm
from MainApp.models import UserProfile
from MainApp.profile_update_views import update_profile

from django.test import TestCase, Client

class ProfileUpdateViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.customer = UserProfile.objects.create(user=self.user, bank_account_no='123456', phone_no='1234567890')

    def test_update_profile_authenticated_user(self):
        url = reverse('update_customer', args=[self.customer.id])
        data = {'first_name': 'John', 'last_name': 'Doe', 'email': 'john@example.com', 'phone_no': '9876543210'}
        request = self.factory.post(url, data)
        request.user = self.user

        response = update_profile(request, self.customer.id)
        self.assertEqual(response.status_code, 302)  # Redirect status code

        # You may want to check if the user's profile has been updated correctly
        updated_user = User.objects.get(id=self.user.id)
        self.assertEqual(updated_user.first_name, 'John')
        self.assertEqual(updated_user.last_name, 'Doe')
        self.assertEqual(updated_user.email, 'john@example.com')
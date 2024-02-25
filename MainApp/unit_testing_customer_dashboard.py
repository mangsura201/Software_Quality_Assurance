from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import UserProfile

class CustomerDashboardTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_customer_dashboard_view(self):
        response = self.client.get(reverse('customer_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Sayma/customer_dashboard.html')
        self.assertEqual(response.context['user'], self.user)

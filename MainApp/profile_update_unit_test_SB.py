from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class YourAppViewsTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Log the user in
        self.client.login(username='testuser', password='testpassword')

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_customer_dashboard_view(self):
        response = self.client.get(reverse('customer_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer_dashboard.html')
        self.assertEqual(response.context['user'], self.user)

    def test_update_profile_view(self):
        response = self.client.get(reverse('update_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_profile.html')

        # Assuming ProfileUpdateForm has some fields, you can test the form submission
        form_data = {'field1': 'value1', 'field2': 'value2'}  # Replace with actual form data
        response = self.client.post(reverse('update_profile'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Assuming a successful form submission redirects to customer_dashboard
        self.assertRedirects(response, reverse('customer_dashboard'))

    def test_logout_view(self):
        response = self.client.get(reverse('logout_view'))
        self.assertEqual(response.status_code, 302)  # Assuming a successful logout redirects to admin_dashboard
        self.assertRedirects(response, reverse('admin_dashboard'))

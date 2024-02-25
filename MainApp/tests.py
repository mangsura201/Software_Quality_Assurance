from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile

class DeleteCustomerViewTest(TestCase):
    def setUp(self):
        # Set up a test client and create a user with a corresponding UserProfile
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.customer = UserProfile.objects.create(user=self.user)

    def test_delete_customer(self):
        """
        Test the deletion of a customer using a POST request.
        """
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Get the delete_customer URL for the specific customer
        url = reverse('delete_customer', args=[self.customer.id])

        # Send a POST request to delete the customer
        response = self.client.post(url)

        # Check if the customer was deleted successfully
        self.assertEqual(response.status_code, 302)  # 302 indicates a successful redirect
        self.assertEqual(UserProfile.objects.filter(id=self.customer.id).exists(), False)
        self.assertEqual(User.objects.filter(id=self.user.id).exists(), False)

        # Check the redirect URL after deletion
        self.assertRedirects(response, reverse('see_all_customers'))

    def test_delete_customer_get_request(self):
        """
        Test rendering the delete_customer.html template for a GET request.
        """
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Get the delete_customer URL for the specific customer
        url = reverse('delete_customer', args=[self.customer.id])

        # Send a GET request, which should render the delete_customer.html template
        response = self.client.get(url)

        # Check if the template is rendered and the customer data is present
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_customer.html')
        self.assertEqual(response.context['customer'], self.customer)

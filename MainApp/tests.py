<<<<<<< HEAD
<<<<<<< HEAD
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile

class DeleteCustomerViewTest(TestCase):
    def setUp(self):
        # Create a test user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a test customer without name and email
        self.customer = UserProfile.objects.create(user=self.user)

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
        self.assertEqual(response.status_code, 200, f"Expected status code 200 but got {response.status_code}")
        self.assertTemplateUsed(response, 'eva/delete_customer.html', f"Template 'delete_customer.html' not used")

        # Check if customer data is present in the context
        self.assertEqual(response.context['customer'], self.customer, "Customer data not present in the context")
=======



>>>>>>> 36d7b73bd8317837136dc243349d904dc80453bf
=======
>>>>>>> 62615bc1b85e5176a07671444b0786e27d168e66

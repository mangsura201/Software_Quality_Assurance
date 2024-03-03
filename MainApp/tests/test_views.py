from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
#from MainApp.forms import CustomerCreationForm, ProfileUpdateForm, MoneyTransferForm, AddMoneyForm

#from .models import UserProfile
from MainApp.models import UserProfile
#from .forms import CustomerCreationForm, ProfileUpdateForm, MoneyTransferForm, AddMoneyForm
#from MainApp.forms import CustomerCreationForm, ProfileUpdateForm, MoneyTransferForm, AddMoneyForm

class CustomerDashboardTestCase(TestCase):
    def setUp(self):
        # Create a sample user profile for testing
        self.user = User.objects.create_user(username='testuser', password='password')
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            bank_account_no='1234567890',
            balance=1000
        )

    def test_customer_dashboard(self):
        # Create a test client
        client = Client()
        
        # Log in the user
        client.login(username='testuser', password='password')

        # Make a GET request to the view
        response = client.get(reverse('customer_dashboard'))

        # Check if the response is successful
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is being used
        self.assertTemplateUsed(response, 'Sayma/customer_dashboard.html')

        # Check if the user details are present in the context
        self.assertEqual(response.context['user'], self.user)


class SeeAllCustomersTestCase(TestCase):
    def setUp(self):
        # Create sample user profiles for testing
        self.user1 = User.objects.create_user(username='user1', password='password1')
        self.profile1 = UserProfile.objects.create(user=self.user1, bank_account_no='123', balance=100)
        
        self.user2 = User.objects.create_user(username='user2', password='password2')
        self.profile2 = UserProfile.objects.create(user=self.user2, bank_account_no='456', balance=200)

    def test_see_all_customers(self):
        # Create a test client
        client = Client()
        
        # Make a GET request to the view
        response = client.get(reverse('see_all_customers'))
        
        # Check if the response is successful
        self.assertEqual(response.status_code, 200)
        
        # Check if the correct template is being used
        self.assertTemplateUsed(response, 'Sayma/see_all_customers.html')
        
        # Check if the customers are present in the context
        customers = response.context['customers']
        self.assertEqual(customers.count(), 2)  # Ensure all customers are retrieved
        
        # Check if the retrieved customers match the expected data
        self.assertIn(self.profile1, customers)
        self.assertIn(self.profile2, customers)
from django.test import RequestFactory 
from .. import views 
class TestHomeView: 
 def test_anonymous(self): 
  req= RequestFactory().get('/') 
  resp=views.HomeView.as_view()(req) 
  assert resp.status_code==200, 'Should be callable by an anyone'
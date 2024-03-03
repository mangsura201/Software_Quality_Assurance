from django.test import TestCase
from django.contrib.auth.models import User
from MainApp.models import UserProfile
from MainApp.forms import CustomerCreationForm, AddMoneyForm


class CustomerCreationFormTest(TestCase):

    def test_form_valid_data(self):
        # Ensure data meets all validation rules (e.g., required fields, unique values)
        form = CustomerCreationForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',  # Unique username is crucial
            'email': 'johndoe@example.com',  # Unique email is important
            'password1': 'password123',
            'password2': 'password123',
            'bank_account_no': '1234567890'  # Assuming 20 characters are required
        })
        self.assertTrue(form.is_valid())  # Assert form is valid

    def test_form_invalid_bank_account_no(self):
        form = CustomerCreationForm(data={
            # ... other fields ...
            'bank_account_no': '123'  # Too short
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['bank_account_no'], ["This field must be exactly 20 characters long."])

    def test_form_save_creates_user_and_profile(self):
        # **Crucial:** Create a valid user and profile beforehand
        user = User.objects.create_user(username='testuser', password='testpassword')
        profile = UserProfile.objects.create(user=user, balance=0)

        form = CustomerCreationForm(data={
            # ... valid data (refer to your form's requirements) ...
        }, instance=profile)  # Associate form with existing profile

        # ... assertions based on the expected behavior of your form's save method ...

class AddMoneyFormTest(TestCase):

    def test_form_valid_data(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        profile = UserProfile.objects.create(user=user, balance=0)
        form = AddMoneyForm(data={'balance': 100}, instance=profile)
        self.assertTrue(form.is_valid())

    def test_form_invalid_negative_balance(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        profile = UserProfile.objects.create(user=user, balance=0)
        form = AddMoneyForm(data={'balance': -50}, instance=profile)
        self.assertFalse(form.is_valid())

        # Validate the actual error message for negative balance
        self.assertEqual(form.errors['balance'], [
            "Ensure this value is greater than or equal to 0."
        ])  # Replace with the actual error message if different

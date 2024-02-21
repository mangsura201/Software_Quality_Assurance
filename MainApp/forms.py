from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class MoneyTransferForm(forms.Form):
    receiver_username = forms.CharField(max_length=150, required=True)
    receiver_email = forms.EmailField(required=True)
    receiver_bank_account_no = forms.CharField(max_length=150, required=True)
    amount = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    sender_bank_account_no = forms.CharField(max_length=150, required=True)
    sender_username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
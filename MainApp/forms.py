from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CustomerCreationForm(UserCreationForm):
    bank_account_no = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        bank_account_no = self.cleaned_data['bank_account_no']
        if commit:
            user.save()
            UserProfile.objects.create(user=user, bank_account_no=bank_account_no)
        return user

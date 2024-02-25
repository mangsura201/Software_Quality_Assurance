from django import forms
from .models import UserProfile, Message

class MoneyTransferForm(forms.Form):
    receiver_username = forms.CharField(max_length=150, required=True)
    receiver_email = forms.EmailField(required=True)
    receiver_bank_account_no = forms.CharField(max_length=150, required=True)
    amount = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    sender_bank_account_no = forms.CharField(max_length=150, required=True)
    sender_username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'subject', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 8}),
        }

from .models import UserProfile

class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_no']  # Fields to be updated

    def save(self, commit=True):
        user = self.instance.user
        user.save()
        return super(CustomerUpdateForm, self).save(commit=commit)

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user', 'bank_account_no', 'balance']  # Excluding fields from the form

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        for field_name in self.Meta.exclude:
            self.fields[field_name].disabled = True  # Disabling excluded fields

    def save(self, commit=True):
        user = self.instance.user
        user.save()
        return super(ProfileUpdateForm, self).save(commit=commit)


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
    

class AddMoneyForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['balance']


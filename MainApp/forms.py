from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CustomerCreationForm(UserCreationForm):
    bank_account_no = forms.CharField(max_length=20, required=True)
    phone_no = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        bank_account_no = self.cleaned_data['bank_account_no']
        phone_no = self.cleaned_data['phone_no']
        if commit:
            user.save()
            UserProfile.objects.create(user=user, bank_account_no=bank_account_no, phone_no=phone_no )
        return user
<<<<<<< HEAD


class CustomerUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = UserProfile
        fields = ['phone_no', 'balance']

    def __init__(self, *args, **kwargs):
        super(CustomerUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name
        self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        user = self.instance.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            return super(CustomerUpdateForm, self).save(commit=commit)
=======
>>>>>>> a6d35c59fa59a3f853a6bb86e2066268f7f1cc94

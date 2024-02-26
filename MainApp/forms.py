from django import forms
from .models import UserProfile, Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

"""Creation of Form for Adding New customer"""
class CustomerCreationForm(UserCreationForm):
    """
    A form for creating a new user with additional fields for bank account number and phone number.

    Inherits:
    ----------
    UserCreationForm : class
        Django's built-in form for user creation.

    Attributes:
    -----------
    bank_account_no : forms.CharField
        Field for entering the bank account number.
    phone_no : forms.CharField
        Field for entering the phone number.

    Meta:
    -----
    model : User
        The model used for the form.
    fields : list of str
        The fields to include in the form.

    Methods:
    --------
    save(self, commit=True)
        Overrides the save method to include saving bank account number and phone number.
    """
    bank_account_no = forms.CharField(max_length=20, required=True)
    phone_no = forms.CharField(max_length=15, required=True)
    """
        Metadata for the form.

        Attributes:
        -----------
        model : User
            The model used for the form.
        fields : list of str
            The fields to include in the form.
        """

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        """
        Saves the user instance along with bank account number and phone number.

        Parameters:
        -----------
        commit : bool, optional
            Indicates whether to save the data to the database immediately.
            Default is True.

        Returns:
        --------
        User
            The user instance that is saved.
        """
        user = super().save(commit=False)
        bank_account_no = self.cleaned_data['bank_account_no']
        phone_no = self.cleaned_data['phone_no']
        if commit:
            user.save()
            UserProfile.objects.create(user=user, bank_account_no=bank_account_no, phone_no=phone_no )
        return user




class AddMoneyForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['balance']


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = UserProfile
        fields = ['phone_no']  # Fields to be updated

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
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
            return super(ProfileUpdateForm, self).save(commit=commit)


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
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = UserProfile
        fields = ['phone_no']  # Fields to be updated

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
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

from pyexpat import model 
from attr import fields
from django import forms 
from . import models 
class PostForm(forms.ModelForm): 
 class Meta: 
  model = models.Post 
  fields=('body',) 
  def clean_body(self): 
   data = self.cleaned_data.get('body') 
   if len(data) <=5: 
    raise forms.ValidationError('Message is too short') 
   return data 



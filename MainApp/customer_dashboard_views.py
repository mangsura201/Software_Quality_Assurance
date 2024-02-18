from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Transaction
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import views as auth_views
from .forms import CustomerCreationForm, ProfileUpdateForm,MoneyTransferForm, AddMoneyForm
from django.contrib.auth import logout
from .models import UserProfile, Transaction
def customer_dashboard(request):
    user = request.user  # Assuming user details are stored in request.user
    return render(request, 'Sayma/customer_dashboard.html', {'user': user})

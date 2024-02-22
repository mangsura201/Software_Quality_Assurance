from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Transaction
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomerCreationForm, CustomerUpdateForm
def customer_dashboard(request):
    # Logic to display customer dashboard
    # Fetch user details, transactions, etc.
    return render(request, 'customer_dashboard.html', context)


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Transaction
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomerCreationForm, CustomerUpdateForm

def customer_dashboard(request):
    user = request.user  # Assuming user details are stored in request.user
    return render(request, 'Sayma/customer_dashboard.html', {'user': user})

def update_profile(request):
    pass
def transaction_details(request):
    pass
def send_money(request):
    pass
def add_money(request):
    pass
def chat_with_admin(request):
    pass

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Transaction
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import views as auth_views
from .forms import CustomerCreationForm, ProfileUpdateForm,MoneyTransferForm, AddMoneyForm
from django.contrib.auth import logout
from .models import UserProfile, Transaction


"""Add Customer"""
#@login_required
def add_customer(request):
    """
    View function to handle adding a new customer.

    This view displays a form to add a new customer and processes the form submission.
    Requires the user to be logged in.

    Parameters:
    -----------
    request : HttpRequest
        The HTTP request object.

    Returns:
    --------
    HttpResponse
        The HTTP response object.
    """
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New customer added successfully!')
            return redirect('admin_dashboard')  # Redirect to admin dashboard after successful addition
    else:
        form = CustomerCreationForm()
    
    return render(request, 'mangsura/add_customer.html', {'form': form})

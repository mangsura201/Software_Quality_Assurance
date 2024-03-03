from django.shortcuts import render

<<<<<<< HEAD
def home(request):
    return render(request, 'home.html')
def customer_transaction(request, a):
    pass

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from django.contrib import messages
from django.contrib.auth import logout

def delete_customer(request, customer_id):
    """
    View function to handle the deletion of a customer.

    Parameters:
    - request: The HTTP request object.
    - customer_id: The ID of the customer to be deleted.

    Returns:
    - If the request method is POST and deletion is successful, redirects to 'see_all_customers'.
    - If the request method is GET, renders the 'delete_customer.html' template with customer data.
    """

    # Retrieve the customer object with the given ID or raise a 404 error if not found
    customer = get_object_or_404(UserProfile, id=customer_id)
    
    if request.method == 'POST':
<<<<<<< HEAD
        # If the request method is POST, delete the associated User object of the customer
        customer.user.delete()
        
        # Display a success message
        messages.success(request, 'Customer deleted successfully!')
        
        # Redirect to 'see_all_customers' after successful deletion
        return redirect('see_all_customers')
    
    # If the request method is GET, render the 'delete_customer.html' template with customer data
    return render(request, 'eva/delete_customer.html', {'customer': customer})
=======
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
>>>>>>> 36d7b73bd8317837136dc243349d904dc80453bf
=======
        # Handle form data and update customer details
        # Redirect to admin dashboard or display success/error messages
        pass  # Your implementation here
    return render(request, 'update_customer.html', context)"""
"""
@login_required
def send_money(request):
    # Logic to send money to a customer account
    if request.method == 'POST':
        # Handle form data and process the money transfer
        # Update sender and receiver account balances
        # Create a transaction record
        # Redirect to admin dashboard or display success/error messages
        pass  # Your implementation here
    return render(request, 'send_money.html', context)

@login_required
def view_transactions(request, user_id):
    # Logic to view all transactions for a specific user
    # Fetch transactions based on user_id
    return render(request, 'view_transactions.html', context)

# Customer Views
@login_required
def customer_dashboard(request):
    # Logic to display customer dashboard
    # Fetch user details, transactions, etc.
    return render(request, 'customer_dashboard.html', context)

@login_required
def update_profile(request):
    # Logic to update customer profile
    if request.method == 'POST':
        # Handle form data and update customer profile
        # Redirect to customer dashboard or display success/error messages
        pass  # Your implementation here
    return render(request, 'update_profile.html', context)

@login_required
def view_own_transactions(request):
    # Logic to view own transactions
    # Fetch transactions for the logged-in customer
    return render(request, 'view_own_transactions.html', context)

@login_required
def send_money_to_customer(request):
    # Logic to send money to another customer's account
    if request.method == 'POST':
        # Handle form data and process the money transfer
        # Update sender and receiver account balances
        # Create a transaction record
        # Redirect to customer dashboard or display success/error messages
        pass  # Your implementation here
    return render(request, 'send_money_to_customer.html', context)

@login_required
def request_zakat(request):
    # Logic to calculate and process zakat request
    # Calculate based on one year's transaction history
    # Display zakat amount or error messages
    return render(request, 'request_zakat.html', context)

# Real-Time Chat Views (if using Django Channels or similar)
# Implement chat functionality for both admin and customers"""
from django.views.generic import TemplateView 
class HomeView(TemplateView): 
 template_name = 'OnlineBankingManagement/base.html' 
>>>>>>> 62615bc1b85e5176a07671444b0786e27d168e66

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Transaction
from django.contrib.auth.models import User
from django.contrib import messages

# Random code for project to Run it perfectly
def home(request):
    return render(request, 'home.html')
def customer_transaction(request, a):
    pass

#@login_required
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
        # If the request method is POST, delete the associated User object of the customer
        customer.user.delete()
        
        # Display a success message
        messages.success(request, 'Customer deleted successfully!')
        
        # Redirect to 'see_all_customers' after successful deletion
        return redirect('see_all_customers')
    
    # If the request method is GET, render the 'delete_customer.html' template with customer data
    return render(request, 'eva/delete_customer.html', {'customer': customer})

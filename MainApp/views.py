from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Transaction
from django.contrib.auth.models import User
from django.contrib import messages
<<<<<<< HEAD
from .forms import CustomerCreationForm, CustomerUpdateForm
=======
from .forms import CustomerCreationForm
>>>>>>> a6d35c59fa59a3f853a6bb86e2066268f7f1cc94

#******************** || Admin Views || **********************
#@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def see_all_customers(request):
    customers = UserProfile.objects.all()
    return render(request, 'see_all_customers.html', {'customers': customers})

def see_all_transactions(request):
    # Logic to retrieve and display all transactions
    pass


<<<<<<< HEAD
def login_to_customer(request):
    # Logic to login to a user (without a password)
    pass


#@login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New customer added successfully!')
            return redirect('admin_dashboard')  # Redirect to admin dashboard after successful addition
    else:
        form = CustomerCreationForm()
    
    return render(request, 'add_customer.html', {'form': form})


#@login_required
def delete_customer(request, customer_id):
    customer = get_object_or_404(UserProfile, id=customer_id)
    
    if request.method == 'POST':
        customer.user.delete()  # Delete the associated User object
        messages.success(request, 'Customer deleted successfully!')
        return redirect('see_all_customers')  # Redirect to see_all_customers after successful deletion
    
    return render(request, 'delete_customer.html', {'customer': customer})


#@login_required
def update_customer(request, customer_id):
    customer = get_object_or_404(UserProfile, id=customer_id)
    if request.method == 'POST':
        form = CustomerUpdateForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer details updated successfully!')
            return redirect('see_all_customers')  # Redirect to see_all_customers after successful update
    else:
        form = CustomerUpdateForm(instance=customer)
    
    return render(request, 'update_customer.html', {'form': form, 'customer': customer})

=======

def login_to_customer(request):
    # Logic to login to a user (without a password)
    pass


#@login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New customer added successfully!')
            return redirect('admin_dashboard')  # Redirect to admin dashboard after successful addition
    else:
        form = CustomerCreationForm()
    
    return render(request, 'add_customer.html', {'form': form})




#@login_required
def delete_customer(request, customer_id):
    # Logic to delete a customer based on customer_id
    # Redirect to admin dashboard or display success/error messages
    pass  # Your implementation here

#@login_required
def update_customer(request, customer_id):
    # Logic to update customer details based on customer_id
    if request.method == 'POST':
        # Handle form data and update customer details
        # Redirect to admin dashboard or display success/error messages
        pass  # Your implementation here
    return render(request, 'update_customer.html')
>>>>>>> a6d35c59fa59a3f853a6bb86e2066268f7f1cc94
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

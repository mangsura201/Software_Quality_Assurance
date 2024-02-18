from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Transaction
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import views as auth_views
from .forms import CustomerCreationForm, ProfileUpdateForm,MoneyTransferForm, AddMoneyForm
from django.contrib.auth import logout
from .models import UserProfile, Transaction

def home(request):
    return render(request, 'home.html')
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
    
    return render(request, 'add_customer.html', {'form': form})





#@login_required
def delete_customer(request, customer_id):
    customer = get_object_or_404(UserProfile, id=customer_id)
    
    if request.method == 'POST':
        customer.user.delete()  # Delete the associated User object
        messages.success(request, 'Customer deleted successfully!')
        return redirect('see_all_customers')  # Redirect to see_all_customers after successful deletion
    
    return render(request, 'delete_customer.html', {'customer': customer})


def add_money(request, customer_id):
    customer = get_object_or_404(UserProfile, id=customer_id)
    if request.method == 'POST':
        form = AddMoneyForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['balance']
            customer.balance += amount
            customer.save()

            # Create Transaction record
            transaction = Transaction.objects.create(
                sender_account_no= "direct from bank",
                receiver_account_no=customer.bank_account_no,
                amount=amount,
                transaction_id = Transaction.generate_unique_transaction_id()  # Function to generate transaction ID
            )
            transaction.save()

            messages.success(request, f'Amount of {amount} transferred successfully to {customer}')
            return redirect('see_all_customers')
    else:
        form = AddMoneyForm()
    return render(request, 'add_money.html', {'form': form})


def customer_transaction(request, customer_id):
    customer = get_object_or_404(UserProfile, id=customer_id)
    user_transactions = Transaction.objects.filter(
        sender_account_no= customer.bank_account_no
    ) | Transaction.objects.filter(
        receiver_account_no= customer.bank_account_no
    ).order_by('-date')  # Assuming 'date' is the field representing the transaction date

    return render(request, 'customer_transaction.html', {'user_transactions': user_transactions})

def see_all_transaction(request):
    if request.user.is_superuser:  # Check if the user is an admin
        all_transactions = Transaction.objects.all().order_by('-date')  # Retrieve all transactions
        return render(request, 'see_all_transaction.html', {'all_transactions': all_transactions})
    else:
        # Handle the case where the user is not an admin (redirect or display an error)
        # For example, redirect to another view or display an error message
        return render(request, 'admin_dashboard.html', {'message': 'You are not authorized to view this page'})
    

#******************** || Customer Views || **********************
def custom_login(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:  # Check if the user is an admin
            return redirect('admin_dashboard')  # Redirect to admin dashboard
        else:
            return redirect('customer_dashboard')  # Redirect to customer dashboard
    else:
        return redirect('login')  # Use default login view for authentication
    
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def customer_dashboard(request):
    user = request.user  # Assuming user details are stored in request.user
    return render(request, 'customer_dashboard.html', {'user': user})

@login_required
def update_profile(request):
    user = request.user.userprofile  # Assuming UserProfile is related to User model
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('customer_dashboard')  # Redirect after successful update
    else:
        form = ProfileUpdateForm(instance=user)
    
    return render(request, 'update_profile.html', {'form': form})


def chat_with_admin(request):
    pass
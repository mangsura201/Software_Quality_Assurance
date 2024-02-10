from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Transaction
from django.contrib.auth.models import User
from django.contrib import messages
<<<<<<< HEAD
from .forms import CustomerCreationForm, CustomerUpdateForm, ProfileUpdateForm,MoneyTransferForm
from django.contrib.auth import logout
from .models import UserProfile, Transaction

=======
from .forms import CustomerCreationForm, CustomerUpdateForm, ProfileUpdateForm
from django.contrib.auth import logout


>>>>>>> 510cdd12fdf308bc09cfeef1c7100c64eff35677
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
#******************** || Customer Views || **********************
def logout_view(request):
    logout(request)
    return redirect('admin_dashboard')

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
"""
def update_profile(request):
    user_profile = request.user # Assuming UserProfile is related to User model
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('customer_dashboard')  # Redirect after successful update
    else:
        form = ProfileUpdateForm(instance=user_profile)
    
    return render(request, 'update_profile.html', {'form': form})
"""

def transaction_details(request):
    pass
<<<<<<< HEAD

@login_required
def money_transfer(request):
    if request.method == 'POST':
        form = MoneyTransferForm(request.POST)
        if form.is_valid():
            receiver_username = form.cleaned_data['receiver_username']
            receiver_email = form.cleaned_data['receiver_email']
            receiver_bank_account_no = form.cleaned_data['receiver_bank_account_no']
            amount = form.cleaned_data['amount']
            sender_bank_account_no = form.cleaned_data['sender_bank_account_no']
            sender_username = form.cleaned_data['sender_username']
            password = form.cleaned_data['password']

            # Verify sender credentials
            sender = request.user.userprofile
            if sender.user.username != sender_username or not sender.user.check_password(password):
                messages.error(request, 'Invalid sender credentials')
                return redirect('money_transfer')

            
            if sender.balance < amount:
                messages.error(request, 'Insufficient balance')
                return redirect('money_transfer')

            receiver = get_object_or_404(UserProfile, user__username=receiver_username, user__email=receiver_email)
            sender.balance -= amount
            receiver.balance += amount
            sender.save()
            receiver.save()

            # Create Transaction record
            transaction = Transaction.objects.create(
                sender_account_no=sender.bank_account_no,
                receiver_account_no=receiver.bank_account_no,
                amount=amount,
                transaction_id = Transaction.generate_unique_transaction_id()  # Function to generate transaction ID
            )
            transaction.save()

            messages.success(request, f'Amount of {amount} transferred successfully to {receiver_username}')
            return redirect('customer_dashboard')
    else:
        form = MoneyTransferForm()

    return render(request, 'money_transfer.html', {'form': form})

=======
def send_money(request):
    pass
>>>>>>> 510cdd12fdf308bc09cfeef1c7100c64eff35677
def add_money(request):
    pass
def chat_with_admin(request):
    pass
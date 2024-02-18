from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Transaction
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import views as auth_views
from .forms import CustomerCreationForm, ProfileUpdateForm,MoneyTransferForm, AddMoneyForm
from django.contrib.auth import logout
from .models import UserProfile, Transaction


def add_money(request, customer_id):
    """
    View function to add money to a customer's balance.

    :param request: HttpRequest object representing the request made to the server.
    :param customer_id: Integer representing the ID of the customer.
    :return: Rendered HTML template with the form for adding money to the customer's balance.
    """
      # Get the customer object using the customer_id
    customer = get_object_or_404(UserProfile, id=customer_id)

    # Check if the request method is POST
    if request.method == 'POST':

         # Initialize the form with the POST data
        form = AddMoneyForm(request.POST)

        # Check if the form is valid
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

             # Display success message

            messages.success(request, f'Amount of {amount} transferred successfully to {customer}')
            return redirect('see_all_customers')
    else:
        # If request method is not POST, initialize an empty form
        form = AddMoneyForm()

     # Render the 'add_money.html' template with the for   
    return render(request, 'mangsura/add_money.html', {'form': form})
from django.shortcuts import get_object_or_404, render, redirect
from .forms import AddMoneyForm
from .models import UserProfile, Transaction
from django.contrib import messages

def add_money(request, customer_id):
    """
    View function to add money to a customer's account.

    Parameters:
    - request (HttpRequest): The HTTP request object.
    - customer_id (int): The ID of the customer whose account will receive the money.

    Returns:
    - If the form is valid and the transaction is successful, redirects to 'see_all_customers' page.
    - If the request method is GET, renders 'mangsura/add_bank_money.html' template with an empty form.
    - If the request method is POST and the form is invalid, re-renders the form with errors.

    Raises:
    - Http404: If the customer with the given ID does not exist.

    Usage:
    - This view is typically mapped to a URL and invoked when a user attempts to add money to a customer's account.
    - It handles both GET and POST requests.
    """
    customer = get_object_or_404(UserProfile, id=customer_id)
    if request.method == 'POST':
        form = AddMoneyForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['balance']
            customer.balance += amount
            customer.save()

            # Create Transaction record
            transaction = Transaction.objects.create(
                sender_account_no="direct from bank",
                receiver_account_no=customer.bank_account_no,
                amount=amount,
                transaction_id=Transaction.generate_unique_transaction_id()  # Function to generate transaction ID
            )
            transaction.save()

            messages.success(request, f'Amount of {amount} transferred successfully to {customer}')
            return redirect('see_all_customers')
    else:
        form = AddMoneyForm()
    return render(request, 'mangsura/add_bank_money.html', {'form': form})

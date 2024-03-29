from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, Transaction
from django.contrib import messages
from .forms import AddMoneyForm
from .models import UserProfile, Transaction

from .models import Transaction

def add_money(request, customer_id):
    customer = get_object_or_404(UserProfile, id=customer_id)
    if request.method == 'POST':
        form = AddMoneyForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['balance']
            customer.balance += amount
            customer.save()

            # Create Transaction record
            transaction = Transaction(sender_account_no="direct from bank",
                                      receiver_account_no=customer.bank_account_no,
                                      amount=amount)
            transaction.save()

            messages.success(request, f'Amount of {amount} transferred successfully to {customer}')
            return redirect('see_all_customers')
    else:
        form = AddMoneyForm()
    return render(request, 'mangsura/add_money.html', {'form': form})
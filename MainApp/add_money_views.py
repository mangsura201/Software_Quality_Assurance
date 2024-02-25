from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Transaction
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import views as auth_views
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
            return redirect('add_money')
    else:
        form = AddMoneyForm()
    return render(request, 'mangsura/add_money.html', {'form': form})
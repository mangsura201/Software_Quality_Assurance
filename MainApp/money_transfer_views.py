from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Transaction
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from .models import UserProfile, Transaction
from .forms import *

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

    return render(request, 'shifat/money_transfer.html', {'form': form})

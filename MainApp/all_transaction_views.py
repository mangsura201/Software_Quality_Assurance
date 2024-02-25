from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from django.contrib import messages
from django.contrib.auth import logout

def see_all_transactions(request):
    if request.user.is_superuser:  # Check if the user is an admin
        all_transactions = Transaction.objects.all().order_by('-date')  # Retrieve all transactions
        return render(request, 'see_all_transaction.html', {'all_transactions': all_transactions})
    else:
        # Handle the case where the user is not an admin (redirect or display an error)
        # For example, redirect to another view or display an error message
        return render(request, 'admin_dashboard.html', {'message': 'You are not authorized to view this page'})
    
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


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
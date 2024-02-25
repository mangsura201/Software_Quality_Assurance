from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import CustomerCreationForm, CustomerUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import logout

def home(request):
    return render(request, 'home.html')

# ******************** || Admin Views || **********************
@login_required
def admin_dashboard(request):
    # Your admin_dashboard implementation goes here
    pass

# Real-Time Chat Views (if using Django Channels or similar)
# Implement chat functionality for both admin and customers
# ...

# ******************** || Customer Views || **********************
def logout_view(request):
    logout(request)
    return redirect('admin_dashboard')

@login_required
def customer_dashboard(request):
    user = request.user  # Assuming user details are stored in request.user
    return render(request, 'customer_dashboard.html', {'user': user})

@login_required
def update_profile(request, customer_id):
    user = get_object_or_404(UserProfile, id=customer_id)  # Assuming UserProfile is related to User model
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            if request.user.is_superuser:  # Check if the user is an admin
                return redirect('admin_dashboard')  # Redirect to admin dashboard
            else:
                return redirect('customer_dashboard')  # Redirect to customer dashboard  # Redirect after successful update
    else:
        form = ProfileUpdateForm(instance=user)
    
    return render(request, 'simita/update_customer.html', {'form': form})

from  django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CustomerCreationForm
from .forms import *


#@login_required
def add_customer(request):
    """
    View function to add a new customer.

    If the request method is POST, the function validates the form data and saves the new customer.
    If the form is valid, a success message is displayed, and the user is redirected to the admin dashboard.
    If the request method is GET, a new instance of the CustomerCreationForm is created.

    :param request: HttpRequest object representing the request made to the server.
    :return: Rendered HTML template with the form for adding a new customer.
    """
    
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New customer added successfully!')
            return redirect('admin_dashboard')  # Redirect to admin dashboard after successful addition
    else:
        form = CustomerCreationForm()

    return render(request, 'mangsura/add_customer.html', {'form': form})

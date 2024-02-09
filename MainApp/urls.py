from django.urls import path
from . import views

urlpatterns = [
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('see_all_customers/', views.see_all_customers, name='see_all_customers'),
    path('see_all_transactions/', views.see_all_transactions, name='see_all_transactions'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('update_customer/<int:customer_id>/', views.update_customer, name='update_customer'),
    path('delete_customer/<int:customer_id>/', views.delete_customer, name='delete_customer'),
    path('login_to_customer/', views.login_to_customer, name='login_to_customer'),
    # Add more URL patterns for other functionalities if needed
]

from django.urls import path
from . import views, see_all_customer_views

urlpatterns = [
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('see_all_users/', views.see_all_users, name='see_all_users'),
    path('see_all_customers/', see_all_customer_views.see_all_customers, name='see_all_customers'),
    path('see_all_transactions/', views.see_all_transactions, name='see_all_transactions'),
    path('add_new_user/', views.add_new_user, name='add_new_user'),
    path('login_to_user/', views.login_to_user, name='login_to_user'),
    # Add more URL patterns for other functionalities if needed
]

from django.urls import path
from . import views

urlpatterns = [
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('see_all_users/', views.see_all_users, name='see_all_users'),
    path('see_all_transactions/', views.see_all_transactions, name='see_all_transactions'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('login_to_user/', views.login_to_user, name='login_to_user'),
    # Add more URL patterns for other functionalities if needed
]

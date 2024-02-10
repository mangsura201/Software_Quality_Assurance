from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('see_all_customers/', views.see_all_customers, name='see_all_customers'),
    path('see_all_transactions/', views.see_all_transactions, name='see_all_transactions'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('update_customer/<int:customer_id>/', views.update_customer, name='update_customer'),
    path('delete_customer/<int:customer_id>/', views.delete_customer, name='delete_customer'),
    

    path('customer_dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('transaction_details/', views.transaction_details, name='transaction_details'),
    path('send_money/', views.send_money, name='send_money'),
    path('add_money/', views.add_money, name='add_money'),
    path('chat_with_admin/', views.chat_with_admin, name='chat_with_admin'),

    # Add more URL patterns for other functionalities if needed
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
]

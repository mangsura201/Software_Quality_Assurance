from django.urls import path
from MainApp import views, money_transfer_views, chat_system_views , see_all_customer_views, customer_dashboard_views



urlpatterns = [
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('see_all_users/', views.see_all_users, name='see_all_users'),
    path('see_all_customers/', see_all_customer_views.see_all_customers, name='see_all_customers'),
    path('customer_dashboard/', customer_dashboard_views.customer_dashboard, name='customer_dashboard'),
    path('see_all_transactions/', views.see_all_transactions, name='see_all_transactions'),
    path('add_new_user/', views.add_new_user, name='add_new_user'),
    path('login_to_user/', views.login_to_user, name='login_to_user'),
    # Add more URL patterns for other functionalities if needed
    path('money_transfer/', money_transfer_views.money_transfer, name='money_transfer'),
    path('inbox/', chat_system_views.inbox, name='inbox'),
    path('sentbox/', chat_system_views.sentbox, name='sentbox'),
    path('send_message/<slug:username>/', chat_system_views.send_message, name='send_message'),
    
]

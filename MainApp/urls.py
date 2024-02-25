from django.urls import path
from MainApp import views, money_transfer_views, chat_system_views, see_all_customer_views, customer_dashboard_views, all_transaction_views, add_customer_views, profile_update_views, login_logout_views
from django.contrib.auth import views as auth_views

from . import views,add_money_views

urlpatterns = [
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('see_all_customers/', see_all_customer_views.see_all_customers, name='see_all_customers'),
    path('customer_dashboard/', customer_dashboard_views.customer_dashboard, name='customer_dashboard'),
    path('see_all_transactions/', all_transaction_views.see_all_transactions, name='see_all_transactions'),
    # Add more URL patterns for other functionalities if needed
    path('money_transfer/', money_transfer_views.money_transfer, name='money_transfer'),
    path('inbox/', chat_system_views.inbox, name='inbox'),
    path('sentbox/', chat_system_views.sentbox, name='sentbox'),
    path('send_message/<slug:username>/', chat_system_views.send_message, name='send_message'),
    

    path('add_money/', add_money_views.add_money, name='add_money'),
    path('add_money/<int:customer_id>/', add_money_views.add_money, name='add_money'),

    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('home/', views.home, name='home'),
    path('', views.home, name='about_us'),
    path('', views.home, name='contact_us'),
    path('', views.home, name='gallery'),
    path('', views.home, name='signup'),
    path('add_customer/', add_customer_views.add_customer, name='add_customer'),
    path('update_customer/<int:customer_id>/', profile_update_views.update_profile, name='update_customer'),
    path('add_money/<int:customer_id>/', add_money_views.add_money, name='add_money'),
    path('delete_customer/<int:customer_id>/', views.delete_customer, name='delete_customer'),
    

    path('customer_dashboard/', customer_dashboard_views.customer_dashboard, name='customer_dashboard'),
    path('update_profile/', profile_update_views.update_profile, name='update_profile'),
    #path('transaction_details/<int:customer_id>/', views.customer_transaction, name='transaction_details'),
    path('money_transfer/', money_transfer_views.money_transfer, name='money_transfer'),
    path('add_money/', add_money_views.add_money, name='add_money'),
    #path('chat_with_admin/', views.chat_with_admin, name='chat_with_admin'),

    # Add more URL patterns for other functionalities if needed
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', login_logout_views.logout_view, name='logout'),
    path('custom_login/', login_logout_views.custom_login, name='custom_login'),

    # Url for testing
    #path('customer_transaction/<int:customer_id>/', views.customer_transaction, name='customer_transaction'),
    #path('see_all_transaction/', views.see_all_transaction, name='see_all_transaction'),
]

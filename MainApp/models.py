from django.db import models
from django.contrib.auth.models import User
import random
import string
from datetime import datetime

# Custom User Profile to Extend Django's User Model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bank_account_no = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)

# Transaction Model
class Transaction(models.Model):
    sender_account_no = models.CharField(max_length=20)
    receiver_account_no = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=8, unique=True)

    def generate_unique_transaction_id(self):
        # Define a function to generate a unique transaction ID
        length = 8  # Length of the transaction ID
        timestamp = str(int(datetime.timestamp(datetime.now())))  # Get current timestamp
        random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length - len(timestamp)))
        transaction_id = timestamp + random_chars
        return transaction_id[:length]  # Ensure the ID length is exactly 8 digits
    
    def save(self, *args, **kwargs):
        # Generate a unique transaction ID before saving
        if not self.transaction_id:
            self.transaction_id = self.generate_unique_transaction_id()
        super().save(*args, **kwargs)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
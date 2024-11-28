from django.db import models

# Customer Model
class Customer(models.Model):
    name = models.CharField(max_length=255)  # Customer's full name
    email = models.EmailField(unique=True)   # Unique email address
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Order Model
class Order(models.Model):
    customer = models.ForeignKey(
        Customer, 
        on_delete=models.CASCADE,  # If a customer is deleted, their orders are also deleted
        related_name='orders'      # Allows reverse lookup (e.g., customer.orders.all())
    )
    order_date = models.DateTimeField(auto_now_add=True)  # Automatically set to the current date and time
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total amount of the order

    def __str__(self):
        return f"Order #{self.id} by {self.customer.name}"

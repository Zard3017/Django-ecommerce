from django.test import TestCase
from ecommerceapp.models import Customer, Order
from django.contrib.auth.models import User

class CustomerOrderTest(TestCase):
    def test_customer_order_relationship(self):
        # Create a Customer
        customer = Customer.objects.create(name="Bradley Lusalenge", email="brad@gmail.com")

        # Create Orders for the Customer
        order1 = Order.objects.create(customer=customer, total_amount=150.00)
        order2 = Order.objects.create(customer=customer, total_amount=200.00)

        # Test the relationships
        self.assertEqual(customer.orders.count(), 2)  # Customer has 2 orders
        self.assertEqual(order1.customer, customer)  # Order1 belongs to the customer
        self.assertEqual(order2.customer, customer)  # Order2 belongs to the customer

# Create your tests here.

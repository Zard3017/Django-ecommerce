from django.shortcuts import render
from .models import Customer

def customer_list(request):
    customers = Customer.objects.all()  # Fetch all customers
    return render(request, 'customer_list.html', {'customers': customers})

# Create your views here.

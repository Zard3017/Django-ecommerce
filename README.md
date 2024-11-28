# E-Commerce Django Project

## Overview
This project is a simple e-commerce application built with Django. It includes models for `Customer` and `Order`, allowing customers to place multiple orders. 

## Features
- Create and manage customers.
- Place orders associated with customers.
- Admin interface for managing customers and orders.

## Technologies Used
- Python 3.x
- Django 4.x (or specify the version you are using)
- SQLite (default database, can be changed to PostgreSQL, MySQL, etc.)
- HTML/CSS (for future front-end development)

## Models
### Customer
- **name**: The name of the customer (string, max length 100).
- **email**: The email address of the customer (string, must be unique).

### Order
- **customer**: Foreign key linking to the `Customer` model (one-to-many relationship).
- **order_date**: The date and time when the order was placed (automatically set).
- **total_amount**: The total amount for the order (decimal).

## Setup Instructions

### Prerequisites
- Python 3.x installed on your machine.
- Basic understanding of Django and how to run a Django project.

### Setting Up the Environment

1. Creating the virtual environment
py -m venv venv

2. Activating the virtual environment
.\.venv\Scripts\Activate.ps1

3. Install django
pip install django

4. Start project Ecommerce
django-admin startproject Ecommerce
cd Ecommerce- to enter the project directory

5. Created my app 
python manage.py startapp ecommerceapp

6. Make migrations and migrate to set up database
python manage.py makemigrations
python manage.py migrate


7. Create a superuser to access the admin interface: included my username,email and password afterwards
python manage.py createsuperuser

8. Run server
python manage.py runserver


The project contains customer_list.html which displays data entered in the django admin dashboard for the orders created, customer and time
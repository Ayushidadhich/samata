"# samata" 
Project Documentation
Project Overview
Introduction
This documentation provides an overview and guide for the samata test project. [Briefly describe the purpose and goals of the project.]

Features

Technologies Used
Django
Django Rest Framework
Djangorestframework-simplejwt
Django-tenant
PostgreSQL

Installation
Prerequisites
Make sure you have the following installed:

Python 3.x
pip

Setup process

1. Create a git clone
    git clone  git clone https://github.com/Ayushidadhich/samata.git

2. Create a virtual enviroment
    python -m venv env

3. Activate your Virtual enviroment:(in window)
  env\Scripts\activate

4. install requirements
    pip install -r requirements.txt
5. Create a django project
    django-admin startproject project name
    cd project name
6.cretae a project api 
    python manage.py startapp app name

7 Run the migrations 
    python manage.py makemigrations
    python manage.py migrate
8.start the server
    python manage.py runserver


sign up json formate:
This view expects a POST request with the following JSON payload:


{
  "email": "user@example.com",
  "phone_number": "+1234567890",
  "password": "StrongPassword123",
  "tenant": "your_tenant_name"
}
    
Test the Login API:
{
    "email": "user@example.com",
    "password": "StrongPassword123"
}
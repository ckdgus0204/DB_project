from django.shortcuts import render
from .models import Book, Customer, Coupon, Search, Buy, Accumulate, Supplier, Supply
from django.db import connection

# Create your views here.

def home(request):
    return render(request,'book/home.html')

def book(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * from book_book")
        rows= cursor.fetchall()
    return render(request,'book/customer.html')

def select_user(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * from Customer",[self.customer])
        row= cursor.fetchone()

    return row
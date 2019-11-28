from django.shortcuts import render
from .models import Book, Coupon, Search, Buy, Accumulate, Supplier, Supply,Buyer
from django.db import connection

# Create your views here.

def home(request):
    return render(request,'book/home.html')

def select_all_book(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * from book_book")
        rows= cursor.fetchall()
    return render(request,'book/book.html',{"books": rows})

def select_all_buyer(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * from book_buyer")
        rows= cursor.fetchall()
    return render(request,'book/buyer.html',{"buyers": rows})

from django.shortcuts import render
from .models import Book, Custumer, Coupon, Search, Buy, Accumulate, Supplier, Supply

# Create your views here.

def home(request):
    
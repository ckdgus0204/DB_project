from django.db import models
from django.utils import timezone
# Create your models here.

class Book(models.Model):
    book_num=models.IntegerField(primary_key=True)
    author=models.CharField(max_length=200)
    book_name=models.CharField(max_length=200)
    publisher= models.CharField(max_length=200)
    stock= models.IntegerField()
    price=models.IntegerField()

class Customer(models.Model):
    c_id=models.CharField(max_length=200,primary_key=True)
    name=models.CharField(max_length=200)
    phone_number=models.IntegerField()
    address= models.CharField(max_length=200)
    password= models.CharField(max_length=200)
    
class Coupon(models.Model):
    coupon_id=models.CharField(max_length=200,primary_key=True)
    discount_percent=models.IntegerField()
    stock=models.IntegerField()
    name= models.CharField(max_length=200)

class Supplier(models.Model):
    supplier_num=models.IntegerField(primary_key =True)
    name=models.CharField(max_length=200)
    phone_number=models.IntegerField()

class Search(models.Model):
    book_num=models.ForeignKey(Book,on_delete=models.CASCADE)
    c_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    search_word=models.CharField(max_length=200)

class Buy(models.Model):
    book_num=models.ForeignKey(Book,on_delete=models.CASCADE)
    c_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    total_price=models.IntegerField()

class Accumulate(models.Model):
    coupon_id=models.ForeignKey(Coupon,on_delete=models.CASCADE)
    c_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    accumulate_date=models.DateField()

class Supply(models.Model):
    book_num=models.ForeignKey(Book,on_delete=models.CASCADE)
    supplier_num=models.ForeignKey(Supplier,on_delete=models.CASCADE)
    supply_date=models.DateField()
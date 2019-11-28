from django import forms
from .models import Book, Coupon, Search, Buy, Accumulate, Supplier, Supply,Buyer

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields={'book_num','author','book_name','publisher','stock','price'}
class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields={'b_id','name','phone_number','address','password'}
class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields={'coupon_id','discount_percent','stock','name'}
class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields={'book_num','id','search_word'}

class BuyForm(forms.ModelForm):
    class Meta:
        model = Search
        fields={'book_num','id','total_price'}
class AccumulateForm(forms.ModelForm):
    class Meta:
        model = Search
        fields={'coupon_id','id','accumulate_date'}
class SupplyForm(forms.ModelForm):
    class Meta:
        model = Search
        fields={'book_num','supplier_num','supply_date'}
class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields={'supplier_num','name','phone_number'}
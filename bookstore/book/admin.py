from django.contrib import admin
from .models import Book, Coupon, Search, Buy, Accumulate, Supplier, Supply,Buyer

# Register your models here.
admin.site.register(Book)

admin.site.register(Coupon)
admin.site.register(Search)
admin.site.register(Buy)
admin.site.register(Accumulate)
admin.site.register(Supplier)
admin.site.register(Supply)
admin.site.register(Buyer)


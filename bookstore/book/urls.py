from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home, name='home'),
    path('buyer/',views.select_all_buyer,name='buyer'),
    path('book/',views.select_all_book,name='book'),
    path('coupon/',views.select_all_book,name='book'),
    path('search/',views.select_all_book,name='book'),
    path('buy/',views.select_all_book,name='book'),
    
    
    
    path('buyer/new/',views.buyer_new,name='buyer_new'),
    path('buyer/new/',views.buyer_new,name='buyer_new'),
    path('buyer/new/',views.buyer_new,name='buyer_new'),
    path('buyer/new/',views.buyer_new,name='buyer_new'),
    path('buyer/new/',views.buyer_new,name='buyer_new'),
    path('buyer/new/',views.buyer_new,name='buyer_new'),
    path('buyer/new/',views.buyer_new,name='buyer_new'),

]
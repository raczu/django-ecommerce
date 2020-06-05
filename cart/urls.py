from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.cart, name='cart'),
    re_path(r'(?P<id>\d+)/$', views.remove_from_cart, name='remove_from_cart'),
    re_path(r'(?P<slug>[\w-]+)/$', views.add_to_cart, name='add_to_cart'),
]

from django.contrib import admin
from django.urls import path, re_path
from . import views

app_name = 'products'

urlpatterns = [
    re_path(r'^$', views.productsList, name='list'),
    re_path(r'^s/$', views.search, name='search'),
    re_path(r'^sale/$', views.productsSale, name='sale'),
    re_path(r'^(?P<cat>[\w-]+)/$', views.category, name='category'),
    re_path(r'^(?P<cat>[\w-]+)/(?P<subcat>[\w-]+)/$', views.subCategory, name='subCategory'),
    re_path(r'^(?P<cat>[\w-]+)/(?P<subcat>[\w-]+)/(?P<slug>[\w-]+)/$', views.productDetail, name='details'),
]

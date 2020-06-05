from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product, Category, ProductImages
import random

def homepage(request):
    products_id_list = list(Product.objects.all().values_list('id', flat=True))
    random_products_id_list = random.sample(products_id_list, min(len(products_id_list), 5))
    random_products = Product.objects.filter(id__in=random_products_id_list)
    template = 'homepage/homepage.html'
    context = {
        'random_products': random_products,
    }
    return render(request, template, context)
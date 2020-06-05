from django.shortcuts import render
from .models import Product, Category, ProductImages
from django.db.models import Q
from django.http import Http404
import random
# Create your views here.

def productsList(request):
    try:
        products = Product.objects.all()
        #category = Category.objects.all()
        #categorylol = Category.objects.filter(title__in=['clothing', 'skate', 'shoes'])
        category = Category.objects.filter(parent__exact=None)
        category_list = list(category)
        sub_category = Category.objects.filter(parent__in=category_list)
        #print(sub_category)
    except:
        #products = None
        raise Http404
    template = 'products/products.html'
    context = {
        'products': products,
        'category': category,
        'sub_category': sub_category,
               }
    return render(request, template, context)
    #     mainCategory = Category.objects.select_related().filter(title = cat)
    #     allCategories = Category.objects.all()
    #     products = Product.objects.all()
    #     template = 'products/products.html'
    #     context = {
    #         'mainCategory': mainCategory,
    #         'allCategories': allCategories,
    #         'products': products,
    #     }
    #     return render(request, template, context)
    # except cat.DoesNotExists:
    #     return productDetail(request, cat)

def productsSale(request):
    try:
        products = Product.objects.all()
        #category = Category.objects.all()
        #categorylol = Category.objects.filter(title__in=['clothing', 'skate', 'shoes'])
        category = Category.objects.filter(parent__exact=None)
        category_list = list(category)
        sub_category = Category.objects.filter(parent__in=category_list)
        #print(sub_category)
    except:
        #products = None
        raise Http404
    template = 'products/sale.html'
    context = {
        'products': products,
        'category': category,
        'sub_category': sub_category,
               }
    return render(request, template, context)

def category(request, cat):
    #print(subCategories)
    try:
        #products = Category.objects.select_related().get(title=cat)
        #products = Category.objects.select_related().get(title=cat).product_set.all()
        products = Product.objects.filter(category__parent__title=cat)
        subCategories = Category.objects.get(title=cat).category_set.all()
    except:
        #products = None
        #subCategories = None
        raise Http404
    template = 'products/category.html'
    context = {
        'products': products,
        'category': cat,
        'subCategories': subCategories
    }
    #print(products)
    return render(request, template, context)

def subCategory(request, cat, subcat):
    try:
        products = Product.objects.filter(category__title=subcat)
        subCategories = Category.objects.get(title=cat).category_set.all()
        #check = Category.objects.filter(title=subcat)
        if not Category.objects.filter(title=subcat).exists():
            raise Http404
    except:
        #products = None
        #subCategories = None
        raise Http404
    template = 'products/category.html'
    context = {
        'products': products,
        'category': cat,
        'subCategory': subcat,
        'subCategories': subCategories,
    }
    print(products)
    #print(subcat)
    #print(subCategories)
    #print(check)
    return render(request, template, context)

def productDetail(request, cat, subcat, slug):
    try:
        products = Product.objects.get(slug=slug)
        # random_products = Product.objects.filter(category__title=subcat)
        products_id_list = list(Product.objects.filter(category__title=subcat).values_list('id', flat=True))
        random_products_id_list = random.sample(products_id_list, min(len(products_id_list), 3))
        random_products = Product.objects.filter(id__in=random_products_id_list)
        # random_products_id_list = random.sample(cat_products_id_list, min(len(cat_products_id_list), 3))
        product_image = ProductImages.objects.filter(product__slug=slug)
    except:
        #products = None
        raise Http404
    template = 'products/productsDetail.html'
    context = {
        'p': products,
        'cat': cat,
        'subcat': subcat,
        'slug': slug,
        'random_products': random_products,
        'product_image': product_image,
        'subcat_s': subcat[:len(subcat)-1],
    }
    return render(request, template, context)

def search(request):
    try:
        s = request.GET['search']
    except:
        s = None
        # raise Http404
    if s:
        products = Product.objects.filter(Q(title__icontains=s) | Q(category__title=s))
    else:
        products = None
    template = 'search/search.html'
    context = {
        'query': s,
        'products': products,
    }
    return render(request, template, context)
    #print(s)
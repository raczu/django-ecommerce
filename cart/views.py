from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

from .models import Cart, Product, CartItem

def cart(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None
    if the_id:
        cart = Cart.objects.get(id=the_id)
        new_total = 0.00
        for item in cart.cartitem_set.all():
            if item.product.sale:
                item.product.price = item.product.sale
            line_total = float(item.product.price) * item.quantity
            new_total += line_total
            #print(item.quantity)
        request.session['items_total'] = cart.cartitem_set.count()
        # print(cart.products.count())
        cart.total = new_total
        cart.save()
        context = {
            'cart': cart
        }
    else:
        emptyMessage = 'YOUR CART IS EMPTY'
        context = {
            'empty': True,
            'emptyMessage': emptyMessage
        }
    #cart = Cart.objects.all()[0]
    template = 'cart/cart.html'
    return render(request, template, context)

def remove_from_cart(request, id):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        return HttpResponseRedirect(reverse('cart'))

    cartitem = CartItem.objects.get(id=id)
    #cartitem.delete()
    cartitem.cart = None
    cartitem.save()
    return HttpResponseRedirect(reverse('cart'))

def add_to_cart(request, slug):
    request.session.set_expiry(12000)
    try:
        qty = request.GET.get('qty')
        update_qty = True
    except:
        qty = None
        update_qty = False
    notes = {}
    try:
        size = request.GET.get('size')
        notes['size'] = size
    except:
        size = None
    try:
        shoe_size = request.GET.get('shoe_size')
        notes['shoe_size'] = shoe_size
    except:
        shoe_size = None
    try:
        skate_size = request.GET.get('skate_size')
        notes['skate_size'] = skate_size
    except:
        skate_size = None
    #print(qty)
    #cart = Cart.objects.all()[0]
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
    cart = Cart.objects.get(id=the_id)
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass
    cartItem, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if created:
        print('yea')
    # if not cartItem in cart.items.all():
    #     cart.items.add(cartItem)
    # else:
    #     cart.items.remove(cartItem)
    if update_qty and qty:
        for key, value in notes.items():
            if value:
                notes = value
                #print(value)
        cartItem.quantity = qty
        cartItem.variation = notes
        cartItem.save()
    else:
        pass
    return HttpResponseRedirect(reverse('cart'))

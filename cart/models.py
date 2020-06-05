from django.db import models

from products.models import Product

# Create your models here.

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    line_total = models.DecimalField(default=2.99, max_digits=1000, decimal_places=2)
    variation = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        try:
            return str(self.cart.id)
        except:
            return str(self.product.title)

class Cart(models.Model):
    #items = models.ManyToManyField(CartItem, blank=True)
    #products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'Cart id: {self.id}'
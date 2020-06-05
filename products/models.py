from django.db import models
import os
from datetime import datetime

# Create your models here.

def get_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{instance.product.slug}-{instance.id}-image.{ext}'
    return os.path.join(
        '%s' % instance.product.slug, filename
    )

def get_upload_path_thumb(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{instance.slug}-{instance.id}-thumbnail.{ext}'
    return os.path.join(
        '%s' % instance.slug, 'thumbnail', filename
    )

class Category(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']
        unique_together = ('slug', 'parent', 'title')
        verbose_name = 'CATEGORY'
        verbose_name_plural = 'Categories'

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    category = models.ForeignKey(Category, blank=True, null=True, related_name='Category', on_delete=models.DO_NOTHING)
    #category = models.ManyToManyField(Category, blank=True, null=True, related_name='Category')
    price = models.DecimalField(decimal_places=2, max_digits=20)
    sale = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to=get_upload_path_thumb, default='doggo.png')
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-update']
        unique_together = ('title', 'slug')
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    # def get_cat_list(self):
    #     k = self.category
    #
    #     breadcrumb = ["masno"]
    #     while k is not None:
    #         breadcrumb.append(k.slug)
    #         k = k.parent
    #     for i in range(len(breadcrumb) - 1):
    #         breadcrumb[i] = ' x '.join(breadcrumb[-1:i - 1:-1])
    #     return breadcrumb[-1:0:-1]

class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = 'image')
    #thumbnail = models.ImageField(upload_to='media/products/')
    image = models.ImageField(upload_to=get_upload_path, default='media/products/szlugson.jpg')

    class Meta:
        verbose_name = 'ADDITIONAL IMAGE'
        verbose_name_plural = 'ADDITIONAL IMAGES'

class VariationManager(models.Manager):
    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size')
    def shoe_sizes(self):
        return super(VariationManager, self).filter(variation_category='shoe_size')
    def skate_sizes(self):
        return super(VariationManager, self).filter(variation_category='skate_size')

VAR_CATEGORIES = {
    ('size', 'size'),
    ('shoe_size', 'shoe_size'),
    ('skate_size', 'skate_size')
}

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=120, choices=VAR_CATEGORIES, default='universal')
    title = models.CharField(max_length=120, blank=True)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    objects = VariationManager()

    class Meta:
        ordering = ['product']

    def __str__(self):
        return self.title



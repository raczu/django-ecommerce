from django.contrib import admin
from django.db import models
from .models import Product, ProductImages, Category, Variation

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title', 'slug']
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('parent', 'title')}

    fieldsets = [
        ('CATEGORIES', {'fields': ['title', 'slug', 'parent']}),
    ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "parent":
            kwargs["queryset"] = Category.objects.order_by('parent__title')
        return super(CategoryAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 0
    max_num = 4

class VariationInline(admin.TabularInline):
    model = Variation
    extra = 0
    max_num = 10

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
    list_display = ['title', 'price', 'update']
    list_editable = ['price']
    readonly_fields = ['date', 'update']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductImagesInline, VariationInline]

    fieldsets = [
        ('PRODUCT INFORMATIONS', {'fields': ['title', 'description', 'category', 'thumbnail', 'slug', 'price', 'sale']}),
        ('DATE INFORMATIONS', {'fields': ['date', 'update']}),

    ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.order_by('parent__title')
        return super(ProductAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

# class VariationAdmin(admin.ModelAdmin):
#     search_fields = ['product', 'title']
#     list_display = ['product', 'title', 'variation_category', 'update']
#     readonly_fields = ['update']
#
#     fieldsets = [
#         ('PRODUCT VALIDATION', {'fields': ['product', 'variation_category', 'title']}),
#         ('DATE INFORMATIONS', {'fields': ['update']}),
#     ]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Variation, VariationAdmin)
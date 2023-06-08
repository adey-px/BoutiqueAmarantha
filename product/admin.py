"""
Customize admin dashboard details to show 
with CategoryAdmin& ProductAdmin as shown below
"""
from django.contrib import admin
from .models import Category, Product


# category fields to display in admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "label")


# product details to display in admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ("sku", "name", "category", "price", "rating", "image")

    # order to appear
    ordering = ("sku",)


# register category & product
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)


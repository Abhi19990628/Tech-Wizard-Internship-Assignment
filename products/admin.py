# products/admin.py
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand_name', 'price')
    search_fields = ('name', 'brand_name')
    list_filter = ('brand_name',)

    # Optional customization to make admin interface more user-friendly
    fields = ('name', 'brand_name', 'price', 'description', 'image_url')

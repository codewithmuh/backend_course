from django.contrib import admin

from .models import Category, Product, order

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name','description', 'created_at', 'updated_at']



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','description', 'price', 'image', 'category', 'created_at', 'updated_at']



@admin.register(order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_name','customer_email', 'product',  'quantity','created_at', 'updated_at']

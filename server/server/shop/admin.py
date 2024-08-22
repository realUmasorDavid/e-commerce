from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'price', 'quantity')
    search_fields = ('id', 'name', 'category', 'price')
    
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'total')
    
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'user', 'amount')
    search_fields = ('id', 'item', 'user', 'amount')
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Cart, CartAdmin)
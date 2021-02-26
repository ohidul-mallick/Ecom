from django.contrib import admin
from .models import Category,Products,Customer,Order
# Register your models here.

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','product','customer','quantity','price','address','phone','date']



# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ['id','name','email','phone','password']
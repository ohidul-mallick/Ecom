from django.contrib import admin
from .models import Category,Products,Customer
# Register your models here.

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']



# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ['id','name','email','phone','password']
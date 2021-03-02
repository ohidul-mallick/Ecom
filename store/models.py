from django.db import models
import datetime
# Create your models here.
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    objects = models.Manager()

    def __str__(self):
        return self.name
    


class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    desc = models.TextField(max_length=500,null=True,blank=True)
    image = models.ImageField(upload_to='Image/Uploads')
    objects = models.Manager()

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=500)
    confirm_password = models.CharField(max_length=500)

    objects = models.Manager()

    @staticmethod
    def get_customer_by_name(name):
        return Customer.objects.get(name=name)
    
    def __str__(self):
        return self.name


class Order(models.Model):
    product=models.ForeignKey(Products, on_delete=models.CASCADE)

    customer = models.ForeignKey(User,on_delete=models.CASCADE) 
    first_name=models.CharField(max_length=50,blank=True,null=True)
    last_name=models.CharField(max_length=50,blank=True,null=True)
    email=models.EmailField(max_length=50,blank=True,null=True)

    quantity = models.IntegerField(default=1)

    price=models.FloatField()

    address=models.CharField(max_length=150,blank=True,null=True)
    phone=models.IntegerField(blank=True,null=True)
    date = models.DateField(default=datetime.datetime.today)
    objects = models.Manager()
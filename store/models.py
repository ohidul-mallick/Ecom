from django.db import models

# Create your models here.

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



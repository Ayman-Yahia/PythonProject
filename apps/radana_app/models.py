from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from ..login_register.models import User
from decimal import Decimal
# Create your models here.

class Cataegory(models.Model):
    cataegory_title=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.cataegory_title





class Item(models.Model):

    title=models.CharField(max_length=100)
    price=models.FloatField()
    description=models.TextField()
    available_quantity=models.IntegerField()
    image=models.ImageField()
    cataegories=models.ForeignKey(Cataegory,related_name='items',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


class Order(models.Model):
    
    #items=models.ManyToManyField(Item,related_name='orders')
    quantity=models.IntegerField()
    user=models.ForeignKey(User, related_name="orders",on_delete=CASCADE)
    items_order=models.ManyToManyField(Item,related_name='orders')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.quantity








# class Order(models.Model):
#     quantity=models.IntegerField(max_length=9)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now=True)
#     order=models.ForeignKey(User,related_name="orders",on_delete=delete.CASCADE)
# def get_image_path(instance, filename):
#     return os.path.join('photos', str(instance.id), filename)

# class Category(models.Model):
#     c_name=models.CharField(max_length=255)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now=True)


# class Product(models.Model):
#     name=models.CharField(max_length=255)
#     desc=models.CharField(max_length=255)
#     price=models.FloatField(max_length=10)
#     available_quantity=models.IntegerField(max_length=10)
#     image=models.ImageField(null=True,blank=True,upload_to=get_image_path)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now=True)
#     cat=models.ForeignKey(Category,related_name="products",on_delete=deletion.CASCADE)
#     Order_Item=models.ManyToManyField(Order,related_name="order1")
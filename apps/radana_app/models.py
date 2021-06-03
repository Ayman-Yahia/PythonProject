from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import OneToOneField
from ..login_register.models import User
from decimal import Decimal
# Create your models here.

class Cataegory(models.Model):
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class Item(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
    description=models.TextField()
    available_quantity=models.IntegerField()
    image=models.CharField(max_length=255)
    categories=models.ForeignKey(Cataegory,related_name='items',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
class Order(models.Model):
    #items=models.ManyToManyField(Item,related_name='orders')
    quantity=models.IntegerField()
    user=models.ForeignKey(User, related_name="orders",on_delete=CASCADE)
    total_price=models.FloatField()
    items_order=models.ManyToManyField(Item,related_name='orders')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.quantity
class Cart(models.Model):
    user=OneToOneField(User,on_delete=CASCADE)
    items=models.ForeignKey(Item,related_name='items',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
# def add_to_cart(user,item):

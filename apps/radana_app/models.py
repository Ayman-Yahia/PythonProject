from django.db import models
from ..login_register.models import User
# Create your models here.
class Order(models.Model):
    quantity=models.IntegerField(max_length=9)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    order=models.ForeignKey(User,related_name="orders",on_delete=delete.CASCADE)
def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Category(models.Model):
    c_name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Product(models.Model):
    name=models.CharField(max_length=255)
    desc=models.CharField(max_length=255)
    price=models.FloatField(max_length=10)
    available_quantity=models.IntegerField(max_length=10)
    image=models.ImageField(null=True,blank=True,upload_to=get_image_path)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    cat=models.ForeignKey(Category,related_name="products",on_delete=deletion.CASCADE)
    Order_Item=models.ManyToManyField(Order,related_name="order1")
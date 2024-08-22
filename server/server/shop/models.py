from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=55)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to="Product_Image")
    price = models.FloatField()
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.name

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    @property
    def total(self):
        self.total = self.product.price * self.quantity
        
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    @property    
    def amount(self):
        self.amount = sum(self.item for self.item in self.item.total) 
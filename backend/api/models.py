from django.db import models
from datetime import datetime

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(default=None)
    price = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField(default=None)

class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    total = models.IntegerField(default=None)
    created_at = models.DateTimeField(default=datetime.now)

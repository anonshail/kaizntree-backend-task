from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Category(models.Model):
    name = models.CharField(max_length=100)

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Item(models.Model):
    sku = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    stock_status = models.CharField(max_length=50)
    available_stock = models.IntegerField()
from sre_constants import CATEGORY
from telnetlib import STATUS
from tkinter import CASCADE
from turtle import mode
from unicodedata import category
from django.db import models

# Create your models here.
#THE TAG MODEL
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    

    # return tag name
    def __str__(self):
        return self.name


#THE CUSTOMER MODEL
class Customers(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    # return customer name
    def __str__(self):
        return self.name

# THE PRODUCT MODEL
class Products(models.Model):
    CATEGORY = (
        ('Indoor Item', 'Indoor Item'),
        ('Out Door Item', 'Out Door Item'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.IntegerField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField(Tag)

    #return product name
    def __str__(self):
        return self.name

# THE ORDERS MODEL
class Orders(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered')
    )
    customer = models.ForeignKey(Customers, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    
    #return order name
    def __str__(self):
        return self.product.name
    


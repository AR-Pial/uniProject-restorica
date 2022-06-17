import numbers
from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User


class Signup(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

def __str__(self):
    return self.name  

class FoodItem(models.Model):
    food_type = models.CharField(max_length=50)
    food_name = models.CharField(max_length=50)
    food_price = models.CharField(max_length=50)

def __str__(self):
    return self.food_name

class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.CharField(max_length=500)

def __str__(self):
    return self.name 

class Order(models.Model):
    order_id = models.CharField(max_length=50)
    item = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    customer_name= models.CharField(max_length=50)

def __str__(self):
    return self.name 

class TableBooking(models.Model):
    
    table_type = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    total_time = models.CharField(max_length=50)

def __str__(self):
    return self.name       
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Product(models.Model):
    categories=(('rte','Ready To Eat'),('rtc','Ready To Cook'))
    cat_choice=models.CharField(max_length=20,choices=categories,default='rte')
    pname=models.CharField(max_length=200)
    image=models.ImageField(upload_to='Products',default='Products/1-1.jpg')
    description=models.TextField()
    price=models.IntegerField()

    def __str__(self):
        return self.pname


class Customer(models.Model):
    customer=models.OneToOneField(User,on_delete=models.CASCADE)
    cust_address=models.CharField(max_length=400,default=None,null=True,blank=True)
    mobile = models.CharField(max_length=12)
    images = models.ImageField(upload_to='Customers',default='Customers/default.jpg')

    def __str__(self):
        return self.customer


class Order(models.Model):
    users=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    pids=models.TextField(null=True)
    delievery_address=models.CharField(max_length=200)
    status=models.IntegerField(default=0)

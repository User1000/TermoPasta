# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime
from django.core.mail import send_mail
from TermoPasta import settings
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30,)
    slug = models.CharField(max_length=40,blank=True, null=True)

    # def save(self):
    #     self.slug = self.name

class Item(models.Model):
    AVAILABLE = (
        ('avail', 'есть в наличии'),
        ('notavail', 'нет в наличии')
    )

    name = models.CharField(max_length=30,)
    shot_desc = models.TextField(blank=True, null=True, max_length=200)
    long_desc = models.TextField(blank=True, null=True, )
    photo = models.ImageField(upload_to='shop/images', blank=True, null=True, default='shop/images/fal.jpg')
    category = models.ForeignKey(Category)
    price = models.IntegerField(default=None, blank=True, null=True )
    available = models.CharField(max_length=10, choices=AVAILABLE, blank=True, null=True, default=None )


class Client(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)


class Order(models.Model):
    client = models.ForeignKey(Client, blank=True, null=True, default=None)
    date = models.DateTimeField()

    def save(self):
        self.date = datetime.now()
        super(Order, self).save()
        send_mail('Order', 'test', settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER],)


class OrderItem(models.Model):
    item = models.ForeignKey(Item)
    quantity = models.IntegerField(default=0)
    order = models.ForeignKey(Order, blank=True, null=True, default=None)


class Test(models.Model):
    item = models.ForeignKey(Item)


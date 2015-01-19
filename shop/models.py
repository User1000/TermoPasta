# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime
from django.core.mail import send_mail
from termopasta import settings
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name=u"Наименование")
    slug = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        verbose_name = u"Категория"
        verbose_name_plural = u"Категории"

    def __unicode__(self):
        return "%s" % (self.name,)

class Item(models.Model):
    AVAILABLE = (
        ('avail', u'есть в наличии'),
        ('notavail', u'нет в наличии')
    )

    name = models.CharField(max_length=60, verbose_name=u"Наименование",)
    shot_desc = models.TextField(blank=True, null=True, max_length=200, verbose_name=u"Краткое описание")
    long_desc = models.TextField(blank=True, null=True, verbose_name = u"Полное описание")
    photo = models.ImageField(upload_to='shop/images', blank=True, null=True, default='shop/images/fal.jpg', verbose_name=u"Фото")
    category = models.ForeignKey(Category, verbose_name=u"Категория")
    price = models.IntegerField(default=None, blank=True, null=True, verbose_name=u"Цена" )
    available = models.CharField(max_length=10, choices=AVAILABLE, blank=True, null=True, default=None, verbose_name=u"Наличие")
    order_index = models.IntegerField(blank=True, null=True, default=-1, verbose_name=u"Индекс сортировки" )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ('-order_index',)

    def __unicode__(self):
        return u"%s (категория: %s, цена: %iгрн)" % (self.name, self.category, self.price)


class Client(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"Имя")
    phone = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"Телефон")
    email = models.CharField(max_length=30, blank=True, null=True)

    def __unicode__(self):
        return u"%s, (тел. %s)" % (self.name or u"Имя не указано", self.phone)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

class Order(models.Model):
    client = models.ForeignKey(Client, blank=True, null=True, default=None, verbose_name=u"Клиент")
    date = models.DateTimeField(verbose_name=u"Дата")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['-date']

    def save(self):
        if self.pk is None:
            self.date = datetime.now()
            send_mail('Order', 'test', settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER],)
        super(Order, self).save()

    def order_items(self):
        return u"%s" % (self.orderitem_set.all()[0] if self.orderitem_set.all()[0:] else u"Нет товаров")
    order_items.short_description = u"Товары"

class OrderItem(models.Model):
    item = models.ForeignKey(Item)
    quantity = models.IntegerField(default=0)
    order = models.ForeignKey(Order, blank=True, null=True, default=None)

    def __unicode__(self):
        return u"%s, количество: %s" % (self.item, self.quantity)


class Test(models.Model):
    item = models.ForeignKey(Item)


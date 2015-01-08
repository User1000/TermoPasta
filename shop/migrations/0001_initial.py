# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True, blank=True)),
                ('phone', models.CharField(max_length=30, null=True, blank=True)),
                ('email', models.CharField(max_length=30, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('shot_desc', models.TextField(max_length=200, null=True, blank=True)),
                ('long_desc', models.TextField(null=True, blank=True)),
                ('photo', models.ImageField(default=b'shop/images/fal.jpg', null=True, upload_to=b'shop/images', blank=True)),
                ('price', models.IntegerField(default=None, null=True, blank=True)),
                ('available', models.CharField(default=None, max_length=10, null=True, blank=True, choices=[(b'avail', b'\xd0\xb5\xd1\x81\xd1\x82\xd1\x8c \xd0\xb2 \xd0\xbd\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x87\xd0\xb8\xd0\xb8'), (b'notavail', b'\xd0\xbd\xd0\xb5\xd1\x82 \xd0\xb2 \xd0\xbd\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x87\xd0\xb8\xd0\xb8')])),
                ('category', models.ForeignKey(to='shop.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('client', models.ForeignKey(default=None, blank=True, to='shop.Client', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.ForeignKey(to='shop.Item')),
                ('order', models.ForeignKey(default=None, blank=True, to='shop.Order', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.ForeignKey(to='shop.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

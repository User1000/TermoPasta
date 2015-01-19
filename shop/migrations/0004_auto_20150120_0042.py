# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_category_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', 'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': '\u041a\u043b\u0438\u0435\u043d\u0442', 'verbose_name_plural': '\u041a\u043b\u0438\u0435\u043d\u0442\u044b'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': '\u0422\u043e\u0432\u0430\u0440', 'verbose_name_plural': '\u0422\u043e\u0432\u0430\u0440\u044b'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-date'], 'verbose_name': '\u0417\u0430\u043a\u0430\u0437', 'verbose_name_plural': '\u0417\u0430\u043a\u0430\u0437\u044b'},
        ),
        migrations.AddField(
            model_name='item',
            name='order_index',
            field=models.IntegerField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=30, null=True, verbose_name='\u0418\u043c\u044f', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=30, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='available',
            field=models.CharField(default=None, choices=[(b'avail', '\u0435\u0441\u0442\u044c \u0432 \u043d\u0430\u043b\u0438\u0447\u0438\u0438'), (b'notavail', '\u043d\u0435\u0442 \u0432 \u043d\u0430\u043b\u0438\u0447\u0438\u0438')], max_length=10, blank=True, null=True, verbose_name='\u041d\u0430\u043b\u0438\u0447\u0438\u0435'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', to='shop.Category'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='long_desc',
            field=models.TextField(null=True, verbose_name='\u041f\u043e\u043b\u043d\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=30, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(default=b'shop/images/fal.jpg', upload_to=b'shop/images', null=True, verbose_name='\u0424\u043e\u0442\u043e', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=None, null=True, verbose_name='\u0426\u0435\u043d\u0430', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='shot_desc',
            field=models.TextField(max_length=200, null=True, verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(default=None, blank=True, to='shop.Client', null=True, verbose_name='\u041a\u043b\u0438\u0435\u043d\u0442'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430'),
            preserve_default=True,
        ),
    ]

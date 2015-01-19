# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20150120_0042'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('-order_index',), 'verbose_name': '\u0422\u043e\u0432\u0430\u0440', 'verbose_name_plural': '\u0422\u043e\u0432\u0430\u0440\u044b'},
        ),
        migrations.AlterField(
            model_name='item',
            name='order_index',
            field=models.IntegerField(default=-1, null=True, verbose_name='\u0418\u043d\u0434\u0435\u043a\u0441 \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438', blank=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0013_produto_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='concluido',
            field=models.BooleanField(default=False),
        ),
    ]

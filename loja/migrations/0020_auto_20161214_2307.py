# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-15 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0019_auto_20161214_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(upload_to='loja/static/product_images'),
        ),
    ]
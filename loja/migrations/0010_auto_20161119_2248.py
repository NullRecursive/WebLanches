# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0009_auto_20161117_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantidade', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meus_itens', models.TextField(null=True)),
                ('usuario', models.ForeignKey(to='loja.Usuario')),
            ],
        ),
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(upload_to='loja/static/product_images'),
        ),
        migrations.AddField(
            model_name='item',
            name='id_produto',
            field=models.ForeignKey(to='loja.Produto'),
        ),
    ]

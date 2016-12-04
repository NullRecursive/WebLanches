# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0011_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='meus_itens',
        ),
        migrations.AddField(
            model_name='item',
            name='id_pedido',
            field=models.ForeignKey(default=0, to='loja.Pedido'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='data_do_pedido',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='item',
            name='id_produto',
            field=models.ForeignKey(default=0, to='loja.Produto'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='usuario',
            field=models.ForeignKey(default=0, to='loja.Usuario'),
        ),
    ]

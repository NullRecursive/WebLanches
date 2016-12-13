# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0016_auto_20161204_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='estado_do_pedido',
            field=models.CharField(choices=[('em_andamento', 'Em Andamento'), ('concluido', 'Concluido'), ('finalizado', 'Finalizado'), ('em_entrega', 'Em Entrega'), ('encerrado', 'Encerrado')], max_length=12, default='em_andamento'),
        ),
    ]

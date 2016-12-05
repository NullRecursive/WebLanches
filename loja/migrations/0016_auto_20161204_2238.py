# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0015_auto_20161204_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='concluido',
        ),
        migrations.AddField(
            model_name='pedido',
            name='estado_do_pedido',
            field=models.CharField(default=('em_andamento', 'Em Andamento'), max_length=12, choices=[('em_andamento', 'Em Andamento'), ('concluido', 'Concluido'), ('finalizado', 'Finalizado'), ('em_entrega', 'Em Entrega'), ('encerrado', 'Encerrado')]),
        ),
    ]

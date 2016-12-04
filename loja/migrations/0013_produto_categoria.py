# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0012_auto_20161204_0303'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.CharField(default=('hamburguer', 'Hambuguer'), choices=[('hamburguer', 'Hambuguer'), ('bebida', 'Bebida'), ('pastel', 'Pastel'), ('pizzas', 'Pizzas')], max_length=10),
        ),
    ]

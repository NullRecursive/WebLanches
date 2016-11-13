# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0002_usuario_endereco'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='cep',
            field=models.CharField(default='', max_length=8),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_usuario_cep'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.TextField()),
                ('preco', models.FloatField()),
                ('descricao', models.TextField()),
                ('imagem', models.ImageField(upload_to=b'')),
            ],
        ),
    ]

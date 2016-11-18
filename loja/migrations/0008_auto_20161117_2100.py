# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0007_auto_20161117_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='id',
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=250, serialize=False, primary_key=True),
        ),
    ]

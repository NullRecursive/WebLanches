# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0005_auto_20161117_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='emFalta',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]

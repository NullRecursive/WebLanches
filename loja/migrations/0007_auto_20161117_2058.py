# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0006_produto_emfalta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='emFalta',
            new_name='em_Falta',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klient', '0003_remove_klient_catkli'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klient',
            name='nazwa',
            field=models.CharField(max_length=30, blank=True, unique=True),
        ),
    ]

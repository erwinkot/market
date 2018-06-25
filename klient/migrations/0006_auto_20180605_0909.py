# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klient', '0005_auto_20180604_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lokacja',
            name='adres',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='lokacja',
            name='kodpocztowy',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='lokacja',
            name='nazwa',
            field=models.CharField(max_length=40, blank=True, unique=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producent',
            name='numer',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='producent',
            name='ulica',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='producent',
            name='firma',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='producent',
            name='kodpocztowy',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='producent',
            name='kraj',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='producent',
            name='miasto',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]

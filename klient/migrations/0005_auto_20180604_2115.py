# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klient', '0004_auto_20180602_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='klient',
            name='rodzplat',
            field=models.CharField(choices=[('gotówka', 'gotówka'), ('przelew', 'przelew')], default='gotówka', max_length=20),
        ),
        migrations.AddField(
            model_name='lokacja',
            name='dnidostawy',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='lokacja',
            name='dzienodciecia',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='lokacja',
            name='godzdostawy',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='lokacja',
            name='nazwa',
            field=models.CharField(unique=True, max_length=40),
        ),
    ]

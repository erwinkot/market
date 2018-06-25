# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klient', '0002_grupa'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='grupa',
            field=models.ForeignKey(default=0, related_name='profiles', to='klient.Grupa', blank=True),
        ),
    ]

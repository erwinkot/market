# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_grupa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='grupa',
            field=models.ForeignKey(blank=True, to='klient.Grupa', related_name='profiles', default=1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='klient',
            field=models.ForeignKey(blank=True, to='klient.Klient', related_name='profiles', default=1),
        ),
    ]

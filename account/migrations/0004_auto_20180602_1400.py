# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20180531_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='grupa',
            field=models.ForeignKey(to='klient.Grupa', related_name='profiles', default=1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='klient',
            field=models.ForeignKey(to='klient.Klient', related_name='profiles', default=1),
        ),
    ]

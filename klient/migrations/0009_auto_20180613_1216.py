# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klient', '0008_auto_20180606_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lokacja',
            name='dzienodciecia',
            field=models.CharField(choices=[('poniedziałek', 'poniedziałek'), ('wtorek', 'wtorek'), ('środa', 'środa'), ('czwartek', 'czwartek'), ('piątek', 'piątek')], blank=True, max_length=15),
        ),
    ]

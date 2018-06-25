# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klient', '0006_auto_20180605_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lokacja',
            name='miejscowosc',
            field=models.ForeignKey(default='brak', related_name='lokacjas', to='kontrahent.Miejscowosc'),
        ),
    ]

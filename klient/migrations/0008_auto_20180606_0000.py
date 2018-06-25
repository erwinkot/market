# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klient', '0007_auto_20180605_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lokacja',
            name='miejscowosc',
            field=models.ForeignKey(related_name='lokacjas', default=2, to='kontrahent.Miejscowosc'),
        ),
    ]

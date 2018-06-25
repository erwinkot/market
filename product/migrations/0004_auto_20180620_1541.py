# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20180620_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cotojest',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.DeleteModel(
            name='Cotojest',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klient', '0002_grupa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='klient',
            name='catkli',
        ),
    ]

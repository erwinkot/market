# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20180613_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotojest',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nazwa', models.CharField(max_length=60, unique=True)),
                ('slug', models.SlugField(max_length=70, unique=True)),
            ],
            options={
                'ordering': ('nazwa',),
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='cotojest',
            field=models.ForeignKey(related_name='productsy', to='product.Cotojest'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20180620_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotojest',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nazwa', models.CharField(unique=True, max_length=60)),
                ('slug', models.SlugField(unique=True, max_length=70)),
            ],
            options={
                'ordering': ('nazwa',),
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='cotojest',
            field=models.ForeignKey(to='product.Cotojest', related_name='productsy'),
        ),
    ]

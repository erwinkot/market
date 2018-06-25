# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupa',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nazwa', models.CharField(db_index=True, max_length=40)),
                ('slug', models.SlugField(blank=True)),
            ],
            options={
                'ordering': ('nazwa',),
            },
        ),
    ]

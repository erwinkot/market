# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jh',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=80, db_index=True)),
                ('slug', models.SlugField(max_length=200)),
                ('opis1', models.CharField(blank=True, max_length=80)),
                ('opis2', models.CharField(blank=True, max_length=80)),
                ('opis3', models.CharField(blank=True, max_length=80)),
                ('image', models.ImageField(upload_to='jhs/%Y/%m/%d', blank=True)),
                ('jm', models.CharField(max_length=8)),
                ('ilop', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('nrkat', models.CharField(blank=True, max_length=30)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField(blank=True)),
                ('rabatmax', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('zawart', models.CharField(blank=True, max_length=200)),
                ('label', models.CharField(blank=True, max_length=60)),
                ('status', models.CharField(blank=True, max_length=20)),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Producent',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nazwa', models.CharField(max_length=30, db_index=True)),
                ('slug', models.SlugField(unique=True, max_length=40)),
                ('firma', models.CharField(max_length=100)),
                ('kraj', models.CharField(max_length=60)),
                ('miasto', models.CharField(max_length=30)),
                ('kodpocztowy', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ('nazwa',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nazwa', models.CharField(max_length=60, db_index=True)),
                ('slug', models.SlugField(unique=True, max_length=80)),
                ('cotojest', models.CharField(blank=True, max_length=60)),
                ('kategoria', models.CharField(blank=True, max_length=60)),
                ('shortopis', models.CharField(blank=True, max_length=100)),
                ('opis', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='products/%Y/%m/%d', blank=True)),
                ('fotka', models.URLField(blank=True)),
                ('dokprod1', models.URLField(blank=True)),
                ('dokprod2', models.URLField(blank=True)),
                ('dokprod3', models.URLField(blank=True)),
                ('dokprod4', models.URLField(blank=True)),
                ('pod_vat', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('producent', models.ForeignKey(blank=True, to='product.Producent', related_name='products')),
            ],
            options={
                'ordering': ('nazwa',),
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
        migrations.CreateModel(
            name='Profilmat',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nazwa', models.CharField(max_length=30)),
                ('slug', models.SlugField(unique=True, max_length=40)),
            ],
            options={
                'ordering': ('nazwa',),
            },
        ),
        migrations.AddField(
            model_name='product',
            name='profilmat',
            field=models.ForeignKey(to='product.Profilmat', related_name='productsy'),
        ),
        migrations.AddField(
            model_name='jh',
            name='jh',
            field=models.ForeignKey(to='product.Product', related_name='jhs'),
        ),
        migrations.AlterIndexTogether(
            name='jh',
            index_together=set([('id', 'slug')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrahent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catkli',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nazwa', models.CharField(max_length=60, default='gotówka')),
                ('slug', models.SlugField(blank=True, max_length=66)),
            ],
            options={
                'ordering': ('nazwa',),
            },
        ),
        migrations.CreateModel(
            name='Detale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('rabatz', models.DecimalField(blank=True, max_digits=4, decimal_places=2)),
                ('rabatr', models.DecimalField(blank=True, max_digits=4, decimal_places=2)),
                ('kredytlimit', models.DecimalField(blank=True, max_digits=8, decimal_places=2)),
                ('peyment', models.PositiveIntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Klient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nazwa', models.CharField(db_index=True, blank=True, max_length=30)),
                ('slug', models.SlugField(blank=True)),
                ('firma', models.CharField(max_length=80)),
                ('adres', models.CharField(max_length=60)),
                ('kodpocztowy', models.CharField(max_length=6)),
                ('rodzfirm', models.CharField(choices=[('działalność', 'Jednoosobowa działalność gospodarcza'), ('spółka cywilna', 'Spółka cywilna'), ('spółka jawna', 'Spółka jawna'), ('spółka komandytowa', 'Spółka komandytowa'), ('spółka zoo', 'Spółka z.o.o'), ('spółka akcyjna', 'Spółka akcyjna')], max_length=60, default='działalność')),
                ('nip', models.CharField(max_length=10)),
                ('krs', models.CharField(blank=True, max_length=10)),
                ('ceidg', models.CharField(blank=True, max_length=10)),
                ('regon', models.CharField(blank=True, max_length=9)),
                ('shortopis', models.CharField(blank=True, max_length=200)),
                ('opis', models.TextField(blank=True)),
                ('link2', models.URLField(blank=True)),
                ('status', models.CharField(choices=[('aktywny', 'aktywny'), ('ban', 'ban')], max_length=20, default='aktywny')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('catkli', models.ForeignKey(to='klient.Catkli', related_name='klients')),
                ('miejscowosc', models.ForeignKey(related_name='klientos', blank=True, to='kontrahent.Miejscowosc')),
            ],
            options={
                'ordering': ('nazwa',),
            },
        ),
        migrations.CreateModel(
            name='Lokacja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nazwa', models.CharField(db_index=True, max_length=40)),
                ('slug', models.SlugField(blank=True)),
                ('adres', models.CharField(max_length=60)),
                ('kodpocztowy', models.CharField(max_length=6)),
                ('dzienodciecia', models.CharField(max_length=15)),
                ('godzdostawy', models.CharField(max_length=15)),
                ('shortopis', models.CharField(blank=True, max_length=100)),
                ('link1', models.URLField(blank=True)),
                ('link2', models.URLField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('klient', models.ForeignKey(to='klient.Klient', related_name='lokacjas')),
                ('miejscowosc', models.ForeignKey(related_name='lokacjas', blank=True, to='kontrahent.Miejscowosc')),
            ],
            options={
                'ordering': ('nazwa',),
            },
        ),
        migrations.AddField(
            model_name='detale',
            name='klient',
            field=models.OneToOneField(related_name='detales', to='klient.Klient'),
        ),
    ]

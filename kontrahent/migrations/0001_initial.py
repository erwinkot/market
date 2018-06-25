# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gmina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nazwa', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=150)),
                ('wojt', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'ordering': ('nazwa',),
            },
        ),
        migrations.CreateModel(
            name='Miejscowosc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nazwa', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=150)),
                ('profil', models.CharField(choices=[('miasto', 'Miasto'), ('wieś', 'Wieś')], max_length=30, default='miasto')),
                ('gmina', models.ForeignKey(to='kontrahent.Gmina', related_name='miejscowosci')),
            ],
            options={
                'ordering': ('nazwa',),
            },
        ),
        migrations.CreateModel(
            name='Powiat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nazwa', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=150)),
                ('starosta', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'ordering': ('nazwa',),
            },
        ),
        migrations.CreateModel(
            name='Wojewodztwo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nazwa', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=150)),
                ('wojewoda', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'ordering': ('nazwa',),
            },
        ),
        migrations.AddField(
            model_name='powiat',
            name='wojewodztwo',
            field=models.ForeignKey(to='kontrahent.Wojewodztwo', related_name='powiatos'),
        ),
        migrations.AddField(
            model_name='gmina',
            name='powiat',
            field=models.ForeignKey(to='kontrahent.Powiat', related_name='gminas'),
        ),
    ]

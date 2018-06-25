# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('klient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('czygrupa', models.CharField(default='indywidualny', max_length=30)),
                ('status', models.CharField(default='zamawiający', max_length=30, choices=[('uprawniony', 'Uprawniony'), ('zamawiający', 'Zamawiający')])),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d')),
                ('lokacja', models.CharField(blank=True, max_length=30)),
                ('kodupraw', models.CharField(blank=True, max_length=30)),
                ('activgrup', models.BooleanField(default=False)),
                ('klient', models.ForeignKey(to='klient.Klient', related_name='profiles', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

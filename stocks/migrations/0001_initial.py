# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.FloatField()),
                ('symbol', models.CharField(max_length=100)),
                ('bid', models.DecimalField(decimal_places=5, max_digits=15)),
                ('ask', models.DecimalField(decimal_places=5, max_digits=15)),
                ('exchange', models.PositiveIntegerField(blank=True)),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]
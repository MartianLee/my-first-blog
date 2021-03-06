# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-05 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField(blank=True, null=True)),
                ('trans', models.TextField(blank=True, null=True)),
                ('symbol', models.TextField(blank=True, null=True)),
                ('qty', models.FloatField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'stocks',
                'managed': False,
            },
        ),
    ]

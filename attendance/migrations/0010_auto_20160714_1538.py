# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-14 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0009_auto_20160712_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geodata',
            name='device_id',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='geodata',
            name='latitude',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='geodata',
            name='longitude',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='geodata',
            name='user_id',
            field=models.IntegerField(blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-12 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0008_auto_20160712_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geodata',
            name='device_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='geodata',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='geodata',
            name='longitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='geodata',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]

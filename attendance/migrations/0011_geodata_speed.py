# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-29 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0010_auto_20160714_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='geodata',
            name='speed',
            field=models.FloatField(blank=True, default=0.0),
            preserve_default=False,
        ),
    ]
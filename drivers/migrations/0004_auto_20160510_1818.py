# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0003_remove_driver_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='street_address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='driver',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=10),
        ),
    ]

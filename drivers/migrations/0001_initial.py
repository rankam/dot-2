# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 18:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('last_name', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('middle_initial', models.CharField(max_length=10)),
                ('email_address', models.EmailField(max_length=254, null=True)),
                ('date_of_birth', models.DateField(max_length=8)),
                ('phone_number', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DriverLicense',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=200)),
                ('issuing_state', models.CharField(max_length=10)),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.Driver')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='driver_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.Driver'),
        ),
    ]

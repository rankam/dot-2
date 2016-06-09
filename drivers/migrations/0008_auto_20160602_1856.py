# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0007_auto_20160516_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='driver_id',
            field=models.ForeignKey(related_name='addresses', to='drivers.Driver'),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='driver_id',
            field=models.ForeignKey(related_name='history', to='drivers.Driver'),
        ),
        migrations.AlterField(
            model_name='driverlicense',
            name='driver_id',
            field=models.ForeignKey(related_name='license', to='drivers.Driver'),
        ),
    ]

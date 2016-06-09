# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examiner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examevent',
            name='exam_location',
            field=models.ForeignKey(to='examiner.ExaminerLocation', null=True),
        ),
        migrations.AlterField(
            model_name='examiner',
            name='examiner_type',
            field=models.CharField(max_length=200, choices=[(b'MD', b'MD'), (b'DO', b'DO'), (b'Physician Assistant', b'Physician Assistant'), (b'Chiropractor', b'Chiropractor'), (b'Advanced Practice Nurse', b'Advanced Practice Nurse'), (b'Other Practioner', b'Other (Please Specify)')]),
        ),
        migrations.AlterField(
            model_name='examiner',
            name='honorific',
            field=models.CharField(default=b'dr', max_length=200, choices=[(b'Dr.', b'Dr.'), (b'Mr.', b'Mr.'), (b'Mrs.', b'Mrs.'), (b'Ms.', b'Ms.')]),
        ),
    ]

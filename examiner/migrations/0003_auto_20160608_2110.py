# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-08 21:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('examiner', '0002_auto_20160602_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodpressure',
            name='exam_event',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='examiner.ExamEvent'),
        ),
        migrations.AlterField(
            model_name='examdetermination',
            name='exam_event',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='examiner.ExamEvent'),
        ),
        migrations.AlterField(
            model_name='examquestions',
            name='exam_event',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='examiner.ExamEvent'),
        ),
        migrations.AlterField(
            model_name='hearing',
            name='exam_event',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='examiner.ExamEvent'),
        ),
        migrations.AlterField(
            model_name='physicalexam',
            name='exam_event',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='examiner.ExamEvent'),
        ),
        migrations.AlterField(
            model_name='urinalysis',
            name='exam_event',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='examiner.ExamEvent'),
        ),
        migrations.AlterField(
            model_name='vision',
            name='exam_event',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='examiner.ExamEvent'),
        ),
    ]

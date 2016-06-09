# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 20:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('examiner', '0001_initial'),
        ('drivers', '0006_address_clp_cdl_applicant_holder'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='examiner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='examiner.Examiner'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='blood_clots_bleeding_problems',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='bone_muscle_joint',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='broken_bone',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='cancer',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='chronic_breathing_problems',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='chronic_infection_diseases',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='currently_drink_alcohol',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='diabetes_blood_sugar_problems',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='dizziness_headaches',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='eye_problems',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='eye_surgery',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='failed_drug_test_dependent_illegal_substance',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='fainting_passing_out',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='had_sleep_test',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='head_injury',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='heart_problems',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='heart_procedures',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='high_blood_pressure',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='high_cholesterol',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='insulin_used',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='kidney_problems',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='lung_disease',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='medication',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='mental_health_problems',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='missing_limited_use_limbs',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='neck_back_problems',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='seizure_epilepsy',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='sleep_disorders',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='spent_night_hospital',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='stomach_liver_digestive_problems',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='stroke',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='tabacco_use',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='unexplained_weight_loss',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverhistory',
            name='used_illegal_substances',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no'), ('Not Sure', 'not sure')], default='No', max_length=10),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 20:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drivers', '0006_address_clp_cdl_applicant_holder'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodPressure',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('systolic', models.FloatField()),
                ('diastolic', models.FloatField()),
                ('sitting', models.IntegerField()),
                ('second_reading', models.IntegerField(default=0)),
                ('other', models.CharField(max_length=500, null=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.Driver')),
            ],
        ),
        migrations.CreateModel(
            name='ExamDetermination',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('does_not_meet_standards', models.BooleanField(default=False)),
                ('does_not_meet_standards_description', models.CharField(max_length=500, null=True)),
                ('meets_standards_2_years', models.BooleanField(default=True)),
                ('meets_standards_but_periodic_monitoring_required', models.BooleanField(default=False)),
                ('meets_standards_but_periodic_monitoring_required_reason', models.CharField(max_length=500)),
                ('qualified_for', models.CharField(max_length=200)),
                ('wearing_hearing_aid', models.BooleanField(default=False)),
                ('accompanied_by_a_waiver', models.BooleanField(default=False)),
                ('accompanied_by_a_waiver_reason', models.CharField(max_length=500)),
                ('wearing_corrective_lenses', models.BooleanField(default=False)),
                ('accompanied_by_a_skill_performance_evaluation_SPE_certificate', models.BooleanField(default=False)),
                ('qualified_by_operation_of_49_CFR_391_64_Federal', models.BooleanField(default=False)),
                ('determination_pending', models.BooleanField(default=False)),
                ('determination_pending_reason', models.CharField(max_length=500, null=True)),
                ('return_to_medical_exam_office_for_follow_up_on_must_be_45_days_or_less', models.BooleanField(default=False)),
                ('return_to_medical_exam_office_for_follow_up_on_must_be_45_days_or_less_length', models.IntegerField(default=0)),
                ('medical_examination_report_amended', models.BooleanField(default=False)),
                ('medical_examination_report_amended_reason', models.CharField(max_length=500, null=True)),
                ('if_amended_examiner_signature', models.CharField(max_length=500, null=True)),
                ('if_amended_examiner_signature_date', models.DateTimeField(null=True)),
                ('incomplete_examination', models.BooleanField(default=False)),
                ('incomplete_examination_reason', models.CharField(max_length=500, null=True)),
                ('driving_within_an_exempt_intracity_zone', models.BooleanField(default=False)),
                ('grandfathered_from_state_requirements', models.BooleanField(default=False)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.Driver')),
            ],
        ),
        migrations.CreateModel(
            name='ExamEvent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('passed', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('email_sent', models.BooleanField(default=False)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.Driver')),
            ],
        ),
        migrations.CreateModel(
            name='Examiner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('honorific', models.CharField(choices=[('Dr.', 'dr'), ('Mr.', 'mr'), ('Mrs.', 'mrs'), ('Ms.', 'ms')], default='dr', max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('examiner_type', models.CharField(choices=[('MD', 'md'), ('DO', 'do'), ('Physician Assistant', 'pa'), ('Chiropractor', 'chiro'), ('Advanced Practice Nurse', 'apn'), ('Other Practioner', 'other')], max_length=200)),
                ('examiner_type_description', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExaminerLocation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=10)),
                ('examiner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examiner.Examiner')),
            ],
        ),
        migrations.CreateModel(
            name='ExamQuestions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('height_feet', models.IntegerField()),
                ('height_inches', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('pulse_rate', models.IntegerField()),
                ('pulse_rhythm_regular', models.BooleanField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.Driver')),
                ('exam_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examiner.ExamEvent')),
                ('examiner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examiner.Examiner')),
            ],
        ),
        migrations.CreateModel(
            name='Hearing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hearing_aid_used_for_test_right_ear', models.BooleanField(default=False)),
                ('hearing_aid_used_for_test_left_ear', models.BooleanField(default=False)),
                ('hearing_aid_used_for_test_both_ears', models.BooleanField(default=False)),
                ('whisper_test_right_ear', models.IntegerField(null=True)),
                ('whisper_test_left_ear', models.IntegerField(null=True)),
                ('audiometric_right_ear_500_hz', models.FloatField(null=True)),
                ('audiometric_right_ear_1000_hz', models.FloatField(null=True)),
                ('audiometric_right_ear_2000_hz', models.FloatField(null=True)),
                ('audiometric_left_ear_500_hz', models.FloatField(null=True)),
                ('audiometric_left_ear_1000_hz', models.FloatField(null=True)),
                ('audiometric_left_ear_2000_hz', models.FloatField(null=True)),
                ('audiometric_right_ear_average', models.FloatField(null=True)),
                ('audiometric_left_ear_average', models.FloatField(null=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.Driver')),
                ('exam_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examiner.ExamEvent')),
                ('exam_questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examiner.ExamQuestions')),
                ('examiner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examiner.Examiner')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalExaminerLicense',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('national_registry_number', models.CharField(max_length=200)),
                ('state_license_number', models.CharField(max_length=200)),
                ('issuing_state', models.CharField(max_length=200)),
                ('expiration_date', models.DateTimeField(auto_now=True)),
                ('examiner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examiner.Examiner')),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalExam',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('general', models.BooleanField(default=True)),
                ('skin', models.BooleanField(default=True)),
                ('eyes', models.BooleanField(default=True)),
                ('ears', models.BooleanField(default=True)),
                ('mouth_throat', models.BooleanField(default=True)),
                ('cardiovascular', models.BooleanField(default=True)),
                ('lungs_chest', models.BooleanField(default=True)),
                ('abdomen', models.BooleanField(default=True)),
                ('genito_urinary_system_including_hernias', models.BooleanField(default=True)),
                ('back_spine', models.BooleanField(default=True)),
                ('extremities_joins', models.BooleanField(default=True)),
                ('neurological_system_including_reflexes', models.BooleanField(default=True)),
                ('gait', models.BooleanField(default=True)),
                ('vascular_system', models.BooleanField(default=True)),
                ('abnormality_descriptions', models.CharField(max_length=2000)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.Driver')),
                ('exam_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examiner.ExamEvent')),
                ('exam_questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examiner.ExamQuestions')),
                ('examiner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examiner.Examiner')),
            ],
        ),
        migrations.CreateModel(
            name='Urinalysis',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sp_gr', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('blood', models.IntegerField()),
                ('sugar', models.IntegerField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.Driver')),
                ('exam_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examiner.ExamEvent')),
                ('exam_questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examiner.ExamQuestions')),
                ('examiner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examiner.Examiner')),
            ],
        ),
        migrations.CreateModel(
            name='Vision',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('right_eye_uncorrected', models.IntegerField()),
                ('right_eye_corrected', models.IntegerField()),
                ('left_eye_uncorrected', models.IntegerField()),
                ('left_eye_corrected', models.IntegerField()),
                ('both_eyes_corrected', models.IntegerField()),
                ('both_eyes_uncorrected', models.IntegerField()),
                ('right_eye_horizontal_field_of_vision', models.FloatField()),
                ('left_eye_horizontal_field_of_vision', models.FloatField()),
                ('color_blind', models.BooleanField(default=True)),
                ('monocular_vision', models.BooleanField(default=False)),
                ('referred_to_ophthalmologist_or_optometrist', models.BooleanField(default=False)),
                ('received_documentation_from_ophthalmologist_or_optometrist', models.BooleanField(default=False)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.Driver')),
                ('exam_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examiner.ExamEvent')),
                ('exam_questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examiner.ExamQuestions')),
                ('examiner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examiner.Examiner')),
            ],
        ),
        migrations.AddField(
            model_name='examevent',
            name='exam_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examiner.ExaminerLocation'),
        ),
        migrations.AddField(
            model_name='examevent',
            name='examiner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examiner.Examiner'),
        ),
        migrations.AddField(
            model_name='examdetermination',
            name='exam_event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examiner.ExamEvent'),
        ),
        migrations.AddField(
            model_name='examdetermination',
            name='exam_questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examiner.ExamQuestions'),
        ),
        migrations.AddField(
            model_name='examdetermination',
            name='examiner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examiner.Examiner'),
        ),
        migrations.AddField(
            model_name='bloodpressure',
            name='exam_event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examiner.ExamEvent'),
        ),
        migrations.AddField(
            model_name='bloodpressure',
            name='exam_questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examiner.ExamQuestions'),
        ),
        migrations.AddField(
            model_name='bloodpressure',
            name='examiner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examiner.Examiner'),
        ),
    ]
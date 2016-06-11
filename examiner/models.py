from django.db import models
from django.contrib.auth.models import User
# from drivers.models import Driver 

# Create your models here.
class Examiner(models.Model):

	# TODO figure out how to add signature of examiner

	HONORIFICS = (
		('Dr.', 'Dr.'),
		('Mr.', 'Mr.'),
		('Mrs.', 'Mrs.'),
		('Ms.', 'Ms.'),
		)
	TYPES = (
		('MD', 'MD'),
		('DO', 'DO'),
		('Physician Assistant', 'Physician Assistant'),
		('Chiropractor', 'Chiropractor'),
		('Advanced Practice Nurse', 'Advanced Practice Nurse'),
		('Other Practioner', 'Other (Please Specify)'),
		)
	id = models.AutoField(primary_key=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	honorific = models.CharField(choices=HONORIFICS, max_length=200, default='Dr.')
	phone_number = models.CharField(max_length=200)
	examiner_type = models.CharField(choices=TYPES, max_length=200)
	examiner_type_description = models.CharField(max_length=200, null=True)
	
	def __str__(self):
		return "{} {}".format(self.user.first_name, self.user.last_name)

# class ExaminerEmail(models.Model):

# 	id = models.AutoField(primary_key=True)



class MedicalExaminerLicense(models.Model):
	
	id = models.AutoField(primary_key=True)
	national_registry_number = models.CharField(max_length=200)
	state_license_number = models.CharField(max_length=200)
	issuing_state = models.CharField(max_length=200)
	examiner = models.ForeignKey(Examiner)
	expiration_date = models.DateTimeField(auto_now=True)

class ExaminerLocation(models.Model):
	
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	zip_code = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=10)	
	examiner = models.ForeignKey(Examiner)

class ExamEvent(models.Model):
	
	id = models.AutoField(primary_key=True)
	# datetime + _examiner_id
	# unique_id = models.CharField(unique=True, max_length=55)
	# date will be start - end will be date + 30 minutes
	date = models.DateTimeField()
	# driver.name will be the title
	driver = models.ForeignKey('drivers.Driver')
	examiner = models.ForeignKey(Examiner)
	exam_location = models.ForeignKey(ExaminerLocation, null=True)
	passed = models.BooleanField(default=False)
	is_verified = models.BooleanField(default=False) # has the exam been approved
	email_sent = models.BooleanField(default=False)

	def start(self):
		return self.date
		
	def end(self):
		return self.date + 30

class ExamQuestions(models.Model):

	id = models.AutoField(primary_key=True)
	height_feet = models.IntegerField()
	height_inches = models.IntegerField()
	weight = models.IntegerField()
	pulse_rate = models.IntegerField()
	pulse_rhythm_regular = models.BooleanField()
	examiner = models.ForeignKey(Examiner)
	driver = models.ForeignKey('drivers.Driver')	
	exam_event = models.OneToOneField(ExamEvent, on_delete=models.CASCADE)

class BloodPressure(models.Model):
	
	id = models.AutoField(primary_key=True)
	systolic = models.FloatField()
	diastolic = models.FloatField()
	sitting = models.IntegerField()
	second_reading = models.IntegerField(default=0)
	other = models.CharField(max_length=500, null=True)
	examiner = models.ForeignKey(Examiner)
	driver = models.ForeignKey('drivers.Driver')
	exam_event = models.OneToOneField(ExamEvent, on_delete=models.CASCADE)
	


class Urinalysis(models.Model):

	id = models.AutoField(primary_key=True)
	sp_gr = models.IntegerField() # normal is 1
	protein = models.IntegerField() # normal is 0
	blood = models.IntegerField() # normal is 0
	sugar = models.IntegerField() # normal is 0 
	examiner = models.ForeignKey(Examiner)
	driver = models.ForeignKey('drivers.Driver')
	exam_event = models.OneToOneField(ExamEvent, on_delete=models.CASCADE)
	

class Vision(models.Model):
	
	# initial description is 
	# Standard is at least 20/40 acuity (Snellen) in each eye with or without correction. At
	# least 70 field of vision in horizontal meridian measured in each eye. 
	# The use of corrective lenses should be noted on the Medical Examiner's Certificate.	

	id = models.AutoField(primary_key=True)
	right_eye_uncorrected = models.IntegerField()
	right_eye_corrected = models.IntegerField()
	left_eye_uncorrected = models.IntegerField()
	left_eye_corrected = models.IntegerField()
	both_eyes_corrected = models.IntegerField()
	both_eyes_uncorrected = models.IntegerField()
	right_eye_horizontal_field_of_vision = models.FloatField()
	left_eye_horizontal_field_of_vision = models.FloatField()
	color_blind = models.BooleanField(default=True)
	# Applicant can recognize and distinguish among traffic control
	# signals and devices showing red, green, and amber colors
	monocular_vision = models.BooleanField(default=False)
	referred_to_ophthalmologist_or_optometrist = models.BooleanField(default=False)
	received_documentation_from_ophthalmologist_or_optometrist = models.BooleanField(default=False)
	examiner = models.ForeignKey(Examiner)
	driver = models.ForeignKey('drivers.Driver')
	exam_event = models.OneToOneField(ExamEvent, on_delete=models.CASCADE)
	

class Hearing(models.Model):
	# initial description is
	# Standard: Must first perceive whispered voice at not less than 5 feet OR average
	# hearing loss of less than or equal to 40 dB, in better ear (with or without hearing aid).
	
	id = models.AutoField(primary_key=True)
	hearing_aid_used_for_test_right_ear = models.BooleanField(default=False)
	hearing_aid_used_for_test_left_ear = models.BooleanField(default=False)
	hearing_aid_used_for_test_both_ears = models.BooleanField(default=False)
	whisper_test_right_ear = models.IntegerField(null=True)
	whisper_test_left_ear = models.IntegerField(null=True)
	audiometric_right_ear_500_hz = models.FloatField(null=True)
	audiometric_right_ear_1000_hz = models.FloatField(null=True)
	audiometric_right_ear_2000_hz = models.FloatField(null=True)
	audiometric_left_ear_500_hz = models.FloatField(null=True)
	audiometric_left_ear_1000_hz = models.FloatField(null=True)
	audiometric_left_ear_2000_hz = models.FloatField(null=True)
	audiometric_right_ear_average = models.FloatField(null=True)
	audiometric_left_ear_average = models.FloatField(null=True)	
	exam_questions = models.ForeignKey(ExamQuestions)
	driver = models.ForeignKey('drivers.Driver')
	exam_event = models.OneToOneField(ExamEvent, on_delete=models.CASCADE)
	

class PhysicalExam(models.Model):
	# initial description is 
	# The presence of a certain condition may not necessarily disqualify a driver, particularly if the condition is controlled adequately, is not likely to worsen, or
	# is readily amenable to treatment. Even if a condition does not disqualify a driver, the Medical Examiner may consider deferring the driver temporarily.
	# Also, the driver should be advised to take the necessary steps to correct the condition as soon as possible, particularly if neglecting the condition could
	# result in a more serious illness that might affect driving.
	# Check the body systems for abnormalities.

	# True == normal
	# False == abnormal

	id = models.AutoField(primary_key=True)
	general = models.BooleanField(default=True)
	skin = models.BooleanField(default=True)
	eyes = models.BooleanField(default=True)
	ears = models.BooleanField(default=True)
	mouth_throat = models.BooleanField(default=True)
	cardiovascular = models.BooleanField(default=True)
	lungs_chest = models.BooleanField(default=True)
	abdomen = models.BooleanField(default=True)
	genito_urinary_system_including_hernias = models.BooleanField(default=True)
	back_spine = models.BooleanField(default=True)
	extremities_joins = models.BooleanField(default=True)
	neurological_system_including_reflexes = models.BooleanField(default=True)
	gait = models.BooleanField(default=True)
	vascular_system = models.BooleanField(default=True)
	abnormality_descriptions = models.CharField(max_length=2000)
	examiner = models.ForeignKey(Examiner)
	driver = models.ForeignKey('drivers.Driver')
	exam_event = models.OneToOneField(ExamEvent, on_delete=models.CASCADE)
	

class ExamDetermination(models.Model):

	id = models.AutoField(primary_key=True)
	does_not_meet_standards = models.BooleanField(default=False)
	does_not_meet_standards_description = models.CharField(null=True, max_length=500)
	meets_standards_2_years = models.BooleanField(default=True) # Meets standards in 49 CFR 391.41; qualifies for 2-year certificate
	meets_standards_but_periodic_monitoring_required = models.BooleanField(default=False)
	meets_standards_but_periodic_monitoring_required_reason = models.CharField(max_length=500)
	qualified_for = models.CharField(max_length=200)
	wearing_corrective_lenses = models.BooleanField(default=False)
	wearing_hearing_aid = models.BooleanField(default=False)
	accompanied_by_a_waiver = models.BooleanField(default=False)
	accompanied_by_a_waiver_reason = models.CharField(max_length=500)
	wearing_corrective_lenses = models.BooleanField(default=False)
	# Accompanied by a Skill Performance Evaluation (SPE) Certificate
	accompanied_by_a_skill_performance_evaluation_SPE_certificate = models.BooleanField(default=False)
	qualified_by_operation_of_49_CFR_391_64_Federal = models.BooleanField(default=False)
	# (see 49 CFR 391.62) (Federal)
	driving_within_an_exempt_intracity_zone = models.BooleanField(default=False)
	determination_pending = models.BooleanField(default=False)
	determination_pending_reason = models.CharField(max_length=500, null=True)
	return_to_medical_exam_office_for_follow_up_on_must_be_45_days_or_less = models.BooleanField(default=False)
	return_to_medical_exam_office_for_follow_up_on_must_be_45_days_or_less_length = models.IntegerField(default=0)
	medical_examination_report_amended = models.BooleanField(default=False)
	medical_examination_report_amended_reason = models.CharField(max_length=500, null=True)
	if_amended_examiner_signature = models.CharField(max_length=500, null=True)
	if_amended_examiner_signature_date = models.DateTimeField(null=True)
	incomplete_examination = models.BooleanField(default=False)
	incomplete_examination_reason = models.CharField(max_length=500, null=True)
	driving_within_an_exempt_intracity_zone = models.BooleanField(default=False)
	grandfathered_from_state_requirements = models.BooleanField(default=False)
	examiner = models.ForeignKey(Examiner)
	driver = models.ForeignKey('drivers.Driver')
	exam_event = models.OneToOneField(ExamEvent, on_delete=models.CASCADE)
	




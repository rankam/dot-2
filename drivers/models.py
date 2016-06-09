from dateutil.relativedelta import relativedelta
from django.db import models
from examiner.models import Examiner



class Driver(models.Model):

	MALE = 'M'
	FEMALE = 'F'
	GENDERS = ((MALE, 'Male'), (FEMALE, 'Female'))	
	
	id = models.AutoField(primary_key=True)
	last_name = models.CharField(max_length=200)
	first_name = models.CharField(max_length=200)
	middle_initial = models.CharField(max_length=10)
	email_address = models.EmailField(null=True)
	date_of_birth = models.DateField(max_length=8)
	phone_number = models.CharField(max_length=10)
	gender = models.CharField(max_length=10, choices=GENDERS, default=MALE)
	registration_date = models.DateTimeField(auto_now=True)
	examiner = models.ForeignKey(Examiner)

	def __str__(self):
		return self.first_name + ' ' + self.last_name

	
	def calculate_age(self):
		today = date.today()
		delta = relativedelta(today, self.date_of_birth)
		return delta.years

	def date_of_birth_str(self):
		return str(self.date_of_birth)



class Address(models.Model):

	id = models.AutoField(primary_key=True)
	street_address = models.CharField(max_length=200, default='')
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	zip_code = models.CharField(max_length=200)
	timestamp = models.DateTimeField(auto_now=True)
	clp_cdl_applicant_holder = models.BooleanField(default=False)
	driver_id = models.ForeignKey(Driver, related_name='addresses')

class DriverLicense(models.Model):

	id = models.AutoField(primary_key=True)
	number = models.CharField(max_length=200)
	issuing_state = models.CharField(max_length=10)

	timestamp = models.DateTimeField(auto_now=True)
	driver_id = models.ForeignKey(Driver, related_name='license')


class DriverHistory(models.Model):
	DRIVERHISTORYCHOICES = (
		('Yes', 'yes'),
		('No', 'no'),
		('Not Sure', 'not sure')
		)
	id = models.AutoField(primary_key=True)
	eye_surgery = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	eye_surgery_description = models.TextField(max_length=500, default=None, null=True)
	medication = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	medication_description = models.TextField(max_length=500, default=None, null=True)
	head_injury = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	seizure_epilepsy = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	eye_problems = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	heart_problems = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	heart_procedures = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	high_blood_pressure = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	high_cholesterol = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	chronic_breathing_problems = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	lung_disease = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	kidney_problems = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	stomach_liver_digestive_problems = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	diabetes_blood_sugar_problems = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	insulin_used = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	mental_health_problems = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	fainting_passing_out = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	dizziness_headaches = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	unexplained_weight_loss = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	stroke = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	missing_limited_use_limbs = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	neck_back_problems = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	bone_muscle_joint = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	blood_clots_bleeding_problems = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	cancer = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	chronic_infection_diseases = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	sleep_disorders = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	had_sleep_test = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	spent_night_hospital = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	broken_bone = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	tabacco_use = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	currently_drink_alcohol = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	used_illegal_substances = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	failed_drug_test_dependent_illegal_substance = models.CharField(max_length=10, choices=DRIVERHISTORYCHOICES, default='No')
	date_completed = models.DateTimeField(auto_now=True)
	driver_id = models.ForeignKey(Driver, related_name='history')



	
	

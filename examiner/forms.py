import django.forms as forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from examiner.models import *
import django.forms as forms
from drivers.models import DriverHistory
HONORIFICS = (
	('Dr.', 'Dr.'),
	('Mr.', 'Mr.'),
	('Mrs.', 'Mrs.'),
	('Ms.', 'Ms.'),
	)
EXAMINER_TYPES = (
	('MD', 'MD'),
	('DO', 'DO'),
	('Physician Assistant', 'Physician Assistant'),
	('Chiropractor', 'Chiropractor'),
	('Advanced Practice Nurse', 'Advanced Practice Nurse'),
	('Other Practioner', 'Other (Please Specify)'),
	)
STATES = (('OH', 'OH'), ('IN', 'IN'))
GENDER = (('M', 'Male'), ('F', 'Female'))
class ExaminerDriverInformationForm(forms.Form):
	# used so that the examiner can see/update basic driver info

	# personal information
	first_name = forms.CharField() 
	last_name = forms.CharField() 
	middle_initial = forms.CharField(required=False)
	date_of_birth = forms.CharField()
	gender = forms.ChoiceField(choices=GENDER)

	# address information
	street_address = forms.CharField(required=False)
	city = forms.CharField(required=False) 
	state = forms.ChoiceField(choices=STATES, required=False) 
	zip_code = forms.CharField(required=False)	
	
	# driver license information
	driver_license_number = forms.CharField(required=False)
	issuing_state = forms.ChoiceField(choices=STATES, required=False)	

	# contact information
	phone_number = forms.CharField(required=False)
	email_address = forms.CharField(label="Email (only used to confirm your appointment - we won't spam you)", required=False)


class ExaminerDetailsForm(forms.Form):

	first_name = forms.CharField() 
	last_name = forms.CharField() 
	honorific = forms.ChoiceField(choices=HONORIFICS, required=False) 
	phone_number = forms.CharField(required=False)
	examiner_type = forms.ChoiceField(choices=EXAMINER_TYPES, required=False)
	examiner_type_description = forms.CharField(required=False)
	
class ExaminerLocationForm(forms.Form):
	name = forms.CharField(max_length=200)
	address = forms.CharField(max_length=200)
	city = forms.CharField(max_length=200)
	state = forms.CharField(max_length=200)
	zip_code = forms.CharField(max_length=200)
	phone_number = forms.CharField(max_length=10)	

class ExaminerRegistrationForm(UserCreationForm):

    class Meta:
    	model = User
    	fields = ("username", "first_name", "last_name",)
    	
class ExaminerCompleteRegistrationForm(forms.ModelForm):

	class Meta:
		model = Examiner
		fields = ("honorific", "phone_number", "examiner_type", "examiner_type_description",)

class ExaminerLoginForm(forms.Form):

	email_address = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())

class ExamEventForm(forms.ModelForm):

	class Meta:
		model = ExamEvent
		exclude = ("id", "examiner", "driver", "passed", "is_verified", "email_sent")
        widgets = {
            'date': forms.DateInput(attrs={'class':'datepicker'}),
        }

	# exam_location = models.ForeignKey(ExaminerLocation)
	# passed = models.BooleanField(default=False)
	# is_verified = models.BooleanField(default=False) # has the exam been approved
	# email_sent = models.BooleanField(default=False)

# class MedicalExaminerLicense(forms.ModelForm):
# 	class Meta:
# 		model = MedicalExaminerLicense
# 		exclude = ("id", "examiner", "driver", "exam_event",)

	# id = models.AutoField(primary_key=True)
	# national_registry_number = models.CharField(max_length=200)
	# state_license_number = models.CharField(max_length=200)
	# issuing_state = models.CharField(max_length=200)
	# examiner = models.ForeignKey(Examiner)
	# expiration_date = models.DateTimeField(auto_now=True)

# class ExaminerLocation(forms.ModelForm):
# 	class Meta:
# 		model = ExaminerLocation
# 		exclude = ("id", "examiner", "driver", "exam_event",)

# 	id = models.AutoField(primary_key=True)
# 	name = models.CharField(max_length=200)
# 	address = models.CharField(max_length=200)
# 	city = models.CharField(max_length=200)
# 	state = models.CharField(max_length=200)
# 	zip_code = models.CharField(max_length=200)
# 	phone_number = models.CharField(max_length=10)	
# 	examiner = models.ForeignKey(Examiner)


	CHOICES = (
		('Yes', 'yes'),
		('No', 'no')
		)

class ExamQuestionsForm(forms.ModelForm):
	class Meta:
		model = ExamQuestions
		exclude = ("id", "examiner", "driver", "exam_event", "exam_questions",)



class BloodPressureForm(forms.ModelForm):
	class Meta:
		model = BloodPressure
		exclude = ("id", "examiner", "driver", "exam_event", "exam_questions",)

	


class UrinalysisForm(forms.ModelForm):
	class Meta:
		model = Urinalysis
		exclude = ("id", "examiner", "driver", "exam_event", "exam_questions",)



class VisionForm(forms.ModelForm):
	class Meta:
		model = Vision
		exclude = ("id", "examiner", "driver", "exam_event", "exam_questions",)

	# initial description is 
	# Standard is at least 20/40 acuity (Snellen) in each eye with or without correction. At
	# least 70 field of vision in horizontal meridian measured in each eye. 
	# The use of corrective lenses should be noted on the Medical Examiner's Certificate.	



class HearingForm(forms.ModelForm):
	# initialclass Meta:
	class Meta:
		model = Hearing
		exclude = ("id", "examiner", "driver", "exam_event", "exam_questions",)
		# widgets = {
		# 	# 'hearing_aid_used_for_test_right_ear':forms.RadioSelect()
		# }
	 # description is
	# Standard: Must first perceive whispered voice at not less than 5 feet OR average
	# hearing loss of less than or equal to 40 dB, in better ear (with or without hearing aid).
	


class PhysicalExamForm(forms.ModelForm):
	# initial desc
	class Meta:
		model = PhysicalExam
		exclude = ("id", "examiner", "driver", "exam_event", "exam_questions",)
	# ription is 
	# The presence of a certain condition may not necessarily disqualify a driver, particularly if the condition is controlled adequately, is not likely to worsen, or
	# is readily amenable to treatment. Even if a condition does not disqualify a driver, the Medical Examiner may consider deferring the driver temporarily.
	# Also, the driver should be advised to take the necessary steps to correct the condition as soon as possible, particularly if neglecting the condition could
	# result in a more serious illness that might affect driving.
	# Check the body systems for abnormalities.

	# True == normal
	# False == abnormal

	

class ExamDeterminationForm(forms.ModelForm):
	class Meta:
		model = ExamDetermination
		exclude = ("id", "examiner", "driver", "exam_event", "exam_questions",)





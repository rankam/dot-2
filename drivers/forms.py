import django.forms as forms
from drivers.models import DriverHistory

STATES = (('OH', 'OH'), ('IN', 'IN'))
GENDER = (('M', 'Male'), ('F', 'Female'))
class DriverRegistrationForm(forms.Form):
	
	# personal information
	first_name = forms.CharField() 
	last_name = forms.CharField() 
	middle_initial = forms.CharField(required=False)
	date_of_birth = forms.CharField()
	gender = forms.ChoiceField(choices=GENDER)

	# address information
	street_address = forms.CharField()
	city = forms.CharField() 
	state = forms.ChoiceField(choices=STATES) 
	zip_code = forms.CharField()	
	
	# driver license information
	driver_license_number = forms.CharField()
	issuing_state = forms.ChoiceField(choices=STATES)	

	# contact information
	phone_number = forms.CharField()
	email_address = forms.CharField(label="Email (only used to confirm your appointment - we won't spam you)", required=False)

class DriverHealthHistoryForm(forms.Form):

	CHOICES = (
		('Yes', 'yes'),
		('No', 'no'),
		('Not Sure', 'not sure')
		)

	eye_surgery = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	eye_surgery_description = forms.CharField(widget=forms.Textarea)
	medication = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	medication_description = forms.CharField(widget=forms.Textarea)
	head_injury = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	seizure_epilepsy = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	eye_problems = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	heart_problems = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	heart_procedures = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	high_blood_pressure = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	high_cholesterol = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	chronic_breathing_problems = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	lung_disease = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	kidney_problems = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	stomach_liver_digestive_problems = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	diabetes_blood_sugar_problems = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	insulin_used = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	mental_health_problems = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	fainting_passing_out = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	dizziness_headaches = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	unexplained_weight_loss = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	stroke = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	missing_limited_use_limbs = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	neck_back_problems = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	bone_muscle_joint = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	blood_clots_bleeding_problems = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	cancer = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	chronic_infection_diseases = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	sleep_disorders = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	had_sleep_test = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	spent_night_hospital = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	broken_bone = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	tabacco_use = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	currently_drink_alcohol = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	used_illegal_substances = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')
	failed_drug_test_dependent_illegal_substance = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial='No')






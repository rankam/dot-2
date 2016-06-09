from django.shortcuts import render, redirect
from drivers.forms import DriverRegistrationForm, DriverHealthHistoryForm
from drivers.models import *
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponse
import operator
from functools import reduce

def driver_registration(request):
	form = DriverRegistrationForm()
	if request.method == 'POST':
		driver = Driver(
			last_name=request.POST['last_name'],
			first_name=request.POST['first_name'],
			middle_initial=request.POST['middle_initial'],
			email_address=request.POST['email_address'],
			date_of_birth=request.POST['date_of_birth'],
			phone_number=request.POST['phone_number'],
			gender=request.POST['gender']
			)
		driver.save()
		address = Address(
			street_address=request.POST['street_address'],
			city=request.POST['city'],
			state=request.POST['state'], 
			zip_code=request.POST['zip_code'], 
			driver_id=driver
			)
		address.save()
		driver_license = DriverLicense(
			number=request.POST['driver_license_number'],
			issuing_state=request.POST['issuing_state'],
			driver_id=driver
			)
		driver_license.save()
		request.method = 'GET'
		request.session['driver_id'] = driver.id
		return driver_health_history(request)
	return render(request, 'driver_registration.html', {'form':form})

def driver_update(request):
	if request.method == "POST":
		error = False
		driver_id = request.path.split('/')[-3]
		driver = Driver.objects.get(id=int(driver_id))
		driver.last_name=request.POST['last_name']
		driver.first_name=request.POST['first_name']
		driver.middle_initial=request.POST['middle_initial']
		driver.email_address=request.POST['email_address']
		driver.date_of_birth=request.POST['date_of_birth']
		driver.phone_number=request.POST['phone_number']
		driver.gender=request.POST['gender']
		
		driver.save()

		address = driver.addresses.last()
		if address is not None:
			try:
				address.street_address=request.POST['street_address']
				address.city=request.POST['city']
				address.state=request.POST['state']
				address.zip_code=request.POST['zip_code']
				address.save()

			except:
				error = True
				messages.add_message(request, 40, 'Driver Address Information Not Updated')
				pass
		else:
			try:
				address = Address(
				street_address=request.POST['street_address'],
				city=request.POST['city'],
				state=request.POST['state'],
				zip_code=request.POST['zip_code'],
				driver_id=driver
				)
				address.save()	
			except:
				raise
				error = True			
				messages.add_message(request, 40, 'Driver Address Information Not Updated')
				pass

		driver_license = driver.license.last()
		
		if driver_license is not None:
			try:
				driver_license.number=request.POST['driver_license_number']
				driver_license.issuing_state=request.POST['issuing_state']
				driver_license.save()
			except:
				raise
				error = True
				messages.add_message(request, 40, 'Driver License Information Not Updated')
				pass
		else:
			try:
				driver_license = DriverLicense(
				number=request.POST['driver_license_number'],
				issuing_state=request.POST['issuing_state'],
				driver_id=driver
				)
				driver_license.save()
			except:
				raise
				error = True	
				messages.add_message(request, 40, 'Driver License Information Not Updated')
				pass

		if not error:
			messages.add_message(request, 25, 'Driver Successfully Updated')
		
		return redirect(request.path.replace('update/',''), {'messages':messages})


def driver_health_history(request):
	form = DriverHealthHistoryForm()
	print(request.session['driver_id'])
	if request.method == 'POST':
		print(request.session['driver_id'])
		driver = Driver.objects.get(id=request.session['driver_id'])
		driver_history = DriverHistory(
			eye_surgery=request.POST['eye_surgery'],
			eye_surgery_description=request.POST['eye_surgery_description'],
			medication=request.POST['medication'],
			medication_description=request.POST['medication_description'],
			head_injury=request.POST['head_injury'],
			seizure_epilepsy=request.POST['seizure_epilepsy'],
			eye_problems=request.POST['eye_problems'],
			heart_problems=request.POST['heart_problems'],
			heart_procedures=request.POST['heart_procedures'],
			high_blood_pressure=request.POST['high_blood_pressure'],
			high_cholesterol=request.POST['high_cholesterol'],
			chronic_breathing_problems=request.POST['chronic_breathing_problems'],
			lung_disease=request.POST['lung_disease'],
			kidney_problems=request.POST['kidney_problems'],
			stomach_liver_digestive_problems=request.POST['stomach_liver_digestive_problems'],
			diabetes_blood_sugar_problems=request.POST['diabetes_blood_sugar_problems'],
			insulin_used=request.POST['insulin_used'],
			mental_health_problems=request.POST['mental_health_problems'],
			fainting_passing_out=request.POST['fainting_passing_out'],
			dizziness_headaches=request.POST['dizziness_headaches'],
			unexplained_weight_loss=request.POST['unexplained_weight_loss'],
			stroke=request.POST['stroke'],
			missing_limited_use_limbs=request.POST['missing_limited_use_limbs'],
			neck_back_problems=request.POST['neck_back_problems'],
			bone_muscle_joint=request.POST['bone_muscle_joint'],
			blood_clots_bleeding_problems=request.POST['blood_clots_bleeding_problems'],
			cancer=request.POST['cancer'],
			chronic_infection_diseases=request.POST['chronic_infection_diseases'],
			sleep_disorders=request.POST['sleep_disorders'],
			had_sleep_test=request.POST['had_sleep_test'],
			spent_night_hospital=request.POST['spent_night_hospital'],
			broken_bone=request.POST['broken_bone'],
			tabacco_use=request.POST['tabacco_use'],
			currently_drink_alcohol=request.POST['currently_drink_alcohol'],
			used_illegal_substances=request.POST['used_illegal_substances'],
			failed_drug_test_dependent_illegal_substance=request.POST['failed_drug_test_dependent_illegal_substance'],
			driver_id=driver
			)
		driver_history.save()


	return render(request, 'driver_health_history.html', {'form':form, 'driver_id':request.session['driver_id']})

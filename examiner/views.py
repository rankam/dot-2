from django.shortcuts import render, redirect
from examiner.forms import *
from django.contrib.auth.forms import UserCreationForm
from examiner.forms import *
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.apps import apps
from drivers.models import Driver
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from drivers.forms import DriverRegistrationForm
from functools import reduce
import operator
from django.shortcuts import render, get_object_or_404, render_to_response
from django.db.models import Q
from django.template.loader import render_to_string
import datetime
import json
from django.views.generic import DetailView, UpdateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from examiner.models import *
import simplejson
import datetime
from django.core import serializers



######################################### AUTH
def examiner_logout(request):
    logout(request)
    return redirect('/examiner_register/')


def examiner_login(request):
	form = ExaminerLoginForm()
	if request.method == 'POST':
		username = request.POST['email_address'] 
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			print(user)
			login(request, user=user)
			return redirect('/examiner/{}/calendar/'.format(user.id))

	return render(request, 'examiner_login.html', {'form':form})


def register(request):
	# print(request.user)
	# if request.user:
	# 	return redirect('/examiner/{}'.format(request.user.id))
	if request.method == 'POST':
		form = ExaminerRegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			Examiner(user_id=user.id).save()
			user = authenticate(username=request.POST['username'], password=request.POST['password1'])
			login(request, user)
			return redirect('/examiner/{}/calendar/'.format(user.id))


	else:
		form = ExaminerRegistrationForm()
		return render(request, "examiner_register.html", {
			'form': form,
			})

######################################### AUTH


class DriverDetailView(UpdateView):

    model = Driver
    fields = ('first_name', 'last_name', 'phone_number',)



def update_exam(request):
	if request.method == 'POST':
		exam = ExamEvent.objects.get(id=request.POST['exam_id'])
		for k,v in request.POST.items():
			if k in exam._meta.get_all_field_names():
				converted_val = convert_data_type(exam._meta.get_field(k).get_internal_type(),v)
				setattr(exam, k, converted_val)
		exam.save()
		exam_event = exam_event_to_json(exam)
		return HttpResponse(exam_event)

def delete_exam(request):
	if request.method == 'POST':
		exam = ExamEvent.objects.get(id=request.POST['exam_id'])
		exam.delete()
		return HttpResponse('Success')


def exam_event_to_json(event):
	'''
	We use this to map an event to a calendar event
	'''
	exam_event = {}
	exam_event['title'] = event.driver.first_name + " " + event.driver.last_name
	exam_event['start'] = str(event.date)
	print type(event.date)
	print (event.date + datetime.timedelta(minutes=30))
	print str(event.date + datetime.timedelta(minutes=30))
	exam_event['end'] = str(event.date + datetime.timedelta(minutes=30))
	# stick lets fullcalendar know to keep the appointment visible permantly
	exam_event['phone_number'] = event.driver.phone_number		
	exam_event['first_name'] = event.driver.first_name	
	exam_event['last_name'] = event.driver.last_name	
	exam_event['gender'] = event.driver.gender
	exam_event['email_address'] = event.driver.email_address
	exam_event['date_of_birth'] = str(event.driver.date_of_birth)
	exam_event['hour'] = event.date.hour
	exam_event['minute'] = event.date.minute
	exam_event['id'] = event.id
	if event.date.hour >= 12:
		exam_event['period'] = 'PM'
	else:
		exam_event['period'] = 'AM'
	exam_event['stick'] = True	
	return simplejson.dumps(exam_event)

@login_required(login_url='/examiner/login/')
def submit_exam_questions(request):
	if request.method == 'POST':
		examiner = Examiner.objects.get(id=request.user.id)
		for d in request.POST:
			data = json.loads(d)
		
		# check to see if the driver already exists
		# if they do, there will be a driver_id sent in the post request
		try:
			data['Driver']['id'] = data['Driver'].pop('driver_id')
		except:
			pass
		try:
			driver, created = Driver.objects.get_or_create(**_remove_non_model_fields('Driver', data['Driver']))
		except:
			data['Driver']['examiner'] = examiner
			driver, created = Driver.objects.get_or_create(**_remove_non_model_fields('Driver', data['Driver']))
		# TODO add some sort of date test if this returns an object
		# if examevent.date == today
		if driver.examevent_set.last() is None:
			exam_event = _create_exam_event(examiner, driver)
		else:
			exam_event = driver.examevent_set.last()
		data['ExamQuestions']['driver_id'] = driver.id

		add_driverid_exameventid(driver, exam_event, examiner, data['ExamQuestions'])
		add_driverid_exameventid(driver, exam_event, examiner, data['BloodPressure'])
		add_driverid_exameventid(driver, exam_event, examiner, data['Urinalysis'])
		add_driverid_exameventid(driver, exam_event, examiner, data['Vision'])
		add_driverid_exameventid(driver, exam_event, examiner, data['ExamDetermination'])

		exam_questions, created = ExamQuestions.objects.get_or_create(
			**_remove_non_model_fields('ExamQuestions', data['ExamQuestions'])
			)
		
		bp, created = BloodPressure.objects.get_or_create(
			**_remove_non_model_fields('BloodPressure', data['BloodPressure'])
			)
		ur, created = Urinalysis.objects.get_or_create(
			**_remove_non_model_fields('Urinalysis', data['Urinalysis'])
			)
		vis, created = Vision.objects.get_or_create(
			**_remove_non_model_fields('Vision', data['Vision'])
			)
		exam_det, created = ExamDetermination.objects.get_or_create(
			**_remove_non_model_fields('ExamDetermination', data['ExamDetermination'])
			)


def add_driverid_exameventid(driver, exam_event, examiner, data_dict):
	data_dict['driver_id'] = driver.id
	data_dict['exam_event_id'] = exam_event.id
	data_dict['examiner_id'] = examiner.id

def _remove_non_model_fields(model_name, data_dict):
	print model_name
	if model_name == 'Driver':
		model = apps.get_model('drivers', model_name=model_name)
	else:
		model = apps.get_model('examiner', model_name=model_name)
	return {k:convert_data_type(model._meta.get_field(k).get_internal_type(),v) 
		for k,v in data_dict.items() 
		if k in model._meta.get_all_field_names()
	}
			# model_name = dct['model']
			# if model_name == 'Driver':
			# 	model = apps.get_model('drivers', model_name=model_name)
			# 	try:
			# 		driver_id = int(dct['driver_id'])
			# 		driver = Driver.objects.get(driver_id)
			# 		examiner = driver.examiner
			# 	except:
			# 		driver_id = None
			# else:
			# 	model = apps.get_model('examiner', model_name=model_name)
			# model_fields = {}
			# for k,v in dct.items():
			# 	if k in model._meta.get_all_field_names():
			# 		model_fields[k] = convert_data_type(model._meta.get_field(k).get_internal_type(),v)
			
			# if 'examiner_id' in model._meta.get_all_field_names():
			# 	model_fields['examiner'] = examiner
			# if 'examiner' in model._meta.get_all_field_names():
			# 	model_fields['examiner'] = examiner
			# if 'driver_id' in model._meta.get_all_field_names():
			# 	model_fields['driver_id'] = driver_id
			# if 'exam_event_id' in model._meta.get_all_field_names():
			# 	if driver.examevent_set.last() is None:
			# 		exam_event = _create_exam_event(examiner, driver)
			# 	else:
			# 		exam_event = driver.examevent_set.last()
			# 	model_fields['exam_event_id'] = exam_event.id
			# m = model(**model_fields)
			# m.save()
			# if model_name == 'Driver':
			# 	if driver_id is None:
			# 		driver_id = m.id
			# 		driver = Driver.objects.get(id=driver_id)
			# 		examiner = driver.examiner



def _create_exam_event(examiner, driver):
	exam_event = ExamEvent(date=datetime.datetime.now(),
		driver=driver,examiner=examiner)
	exam_event.save()
	return exam_event




@login_required(login_url='/examiner/login/')
def examiner_drivers(request):
	_drivers = Driver.objects.filter(examiner_id=request.user.id).order_by('first_name')
	paginator = Paginator(_drivers, 10)
	page = request.GET.get('page')
	try:
		drivers = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		drivers = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		drivers = paginator.page(paginator.num_pages)
	if request.method == 'POST':
		print(request)
	return render(request, 'examiner_drivers.html', {'drivers': drivers, 'user':request.user})


@login_required(login_url='/examiner/login/')
def examiner_details(request):
	print(dir(request))
	print(request.user)
	# print(request.get_port())
	print(request.get_host())
	print(request.get_full_path())
	print(request.path)
	form = ExaminerCompleteRegistrationForm()
	if request.method == 'POST' and request.is_ajax():
		form = ExaminerCompleteRegistrationForm(request.POST)
		if form.is_valid():
			print(request.POST)
	return render(request, 'examiner_details.html', {'form':form})

# TODO - FINISH
# figure out how I am going to lookup the driver
# i can likely allow the examiner to search for all drivers
# but on their home page, it should list all of the 
# drivers that have an exam scheduled today
# doing this will allow me to add it to the session
# or i can make the endpoint this /exam_questions/<driver_id>
@login_required(login_url='/examiner/login/')
def exam_questions(request):
	if request.method == 'GET':
		try:
			driver_id = request.path.split('/')[-2]
			driver = Driver.objects.get(id=driver_id)
		except:
			driver = None
		date = datetime.datetime.now().date()
		print(dir(date))
		print date.isoformat()

	return render(request, 'exam_questions.html', {'driver':driver, 'date':str(date.isoformat())})

def convert_data_type(internal_type, value):
	data_types = {
		'IntegerField':lambda x: int(x),
		'CharField': lambda x: str(x),
		'FloatField': lambda x: float(x),
		'DateTimeField': lambda x: datetime.datetime.strptime(value, '%Y-%m-%d %I:%M:%S %p')
	}
	try:
		return data_types[internal_type](value)
	except:
		return value


@login_required(login_url='/examiner/login/')
def get_exam_answers(request):
	'''
	Gets exam answers when a examiner goes back
	Could make sense to store this client side so 
	it isn't necessary to make a call to the db
	'''
	pass

@login_required(login_url='/examiner/login/')
def exam_calendar(request):
	exam_events = []
	exam_event_form = ExamEventForm()
	events = ExamEvent.objects.filter(examiner=Examiner.objects.get(id=request.user.id))
	for event in events:
		exam_event = {}
		exam_event['title'] = event.driver.first_name + " " + event.driver.last_name
		exam_event['start'] = str(event.date)
		exam_event['end'] = str(event.date + datetime.timedelta(minutes=30))
		# stick lets fullcalendar know to keep the appointment visible permantly
		exam_event['phone_number'] = event.driver.phone_number		
		exam_event['first_name'] = event.driver.first_name	
		exam_event['last_name'] = event.driver.last_name	
		exam_event['gender'] = event.driver.gender
		exam_event['email_address'] = event.driver.email_address
		exam_event['date_of_birth'] = str(event.driver.date_of_birth)
		exam_event['hour'] = event.date.hour
		exam_event['minute'] = event.date.minute
		exam_event['id'] = event.id
		if event.date.hour >= 12:
			exam_event['period'] = 'PM'
		else:
			exam_event['period'] = 'AM'
		exam_event['stick'] = True
		exam_events.append(exam_event)

	return render(request, 'exam_calendar.html', {
		'exam_event_form': exam_event_form, 
		'events':simplejson.dumps(exam_events)
		})


	# # date will be start - end will be date + 30 minutes
	# date = models.DateTimeField()
	# # driver.name will be the title
	# driver = models.ForeignKey('drivers.Driver')
	# examiner = models.ForeignKey(Examiner)
	# exam_location = models.ForeignKey(ExaminerLocation, null=True)
	# passed = models.BooleanField(default=False)
	# is_verified = models.BooleanField(default=False) # has the exam been approved
	# email_sent = models.BooleanField(default=False)


def update(request):
	if request.method == 'POST':
		exam_event = ExamEvent.objects.get(id=request.POST['exam_id'])
		print request.POST



def new_exam_from_calendar(request):
	if request.method == 'POST':
		examiner = Examiner.objects.get(id=request.user.id)
		driver_info = {'examiner':examiner}
		exam_info = {'examiner': examiner}
		for k,v in request.POST.items():
			if k in Driver._meta.get_all_field_names():
				driver_info[k] = v
			else:
				exam_info[k] = v
		driver = Driver(**driver_info)
		driver.save()
		exam_hour = exam_info.pop('hour')
		exam_minute = exam_info.pop('minute')
		exam_period = exam_info.pop('period')
		exam_info['date'] = add_hour_minute(exam_info['date'], 
			exam_hour, exam_minute, exam_period)
		exam_info['driver'] = driver
		exam_event = ExamEvent(**exam_info)
		exam_event.save()

		exam_info.pop('driver')
		exam_info.pop('examiner')
		exam_info['title'] = driver.first_name
		exam_info['start'] = exam_info['date']
		exam_info['end'] = str(datetime.datetime.strptime(exam_info['date'], "%Y-%m-%d %H:%M:%S") + datetime.timedelta(minutes=30))	
		# stick lets fullcalendar know to keep the appointment visible permantly
		exam_info['stick'] = True
		return HttpResponse(simplejson.dumps(exam_info),content_type='application/json')
		# return exam_info


		# return HttpResponse(json.dumps(exam_info))

def add_hour_minute(date, hour, minute, period):
	if period.lower() == 'pm' and hour != '12':
		hour = int(hour) + 12
	return '{} {}:{}:00'.format(date, hour, minute)

@login_required(login_url='/examiner/login/')
def examiner_information(request):
	examiner = Examiner.objects.get(id=request.user.id)
	location_forms = []
	details_form = ExaminerDetailsForm({
		'username':examiner.user.username,
		'first_name':examiner.user.first_name,
		'last_name':examiner.user.last_name,
		"honorific": examiner.honorific,
		"phone_number": examiner.phone_number, 
		"examiner_type": examiner.examiner_type, 
		"examiner_type_description": examiner.examiner_type_description,
		})
	for location in examiner.examinerlocation_set.all():
		location_forms.append(
			ExaminerLocationForm({
				'name':location.name,
				'address':location.address,
				'city':location.city,
				'state':location.state,
				'zip_code':location.zip_code,
				'phone_number':location.phone_number
				})
			)
	if len(location_forms) == 0:
		location_forms.append(ExaminerLocationForm())
	return render(request, 'examiner_information.html', {
		'examiner':examiner,
		'details_form':details_form,
		'location_forms':location_forms
		})

def examiner_information_update(request):
	examiner = Examiner.objects.get(id=request.user.id)


@login_required(login_url='/examiner/login/')
def driver_history(request):
	driver_id = request.path.split('/')[-2]
	driver = Driver.objects.get(id=driver_id)
	address = driver.addresses.last()
	license = driver.license.last()
	if address is None and license is None:
		form = ExaminerDriverInformationForm({
				'first_name': driver.first_name,
				'last_name': driver.last_name,
				'middle_initial': driver.middle_initial,
				'date_of_birth': driver.date_of_birth,
				'gender': driver.gender,
				'phone_number': driver.phone_number,
				'email_address': driver.email_address,
			})
	elif address is not None and license is None:
		form = ExaminerDriverInformationForm({
				'first_name': driver.first_name,
				'last_name': driver.last_name,
				'middle_initial': driver.middle_initial,
				'date_of_birth': driver.date_of_birth,
				'gender': driver.gender,
				'street_address': address.street_address,
				'city': address.city,
				'state': address.state,
				'zip_code': address.zip_code,			
				'phone_number': driver.phone_number,
				'email_address': driver.email_address

			})
	elif address is  None and license is not None:
		form = ExaminerDriverInformationForm({
				'first_name': driver.first_name,
				'last_name': driver.last_name,
				'middle_initial': driver.middle_initial,
				'date_of_birth': driver.date_of_birth,
				'gender': driver.gender,
				'driver_license_number': license.number,
				'issuing_state': license.issuing_state,
				'phone_number': driver.phone_number,
				'email_address': driver.email_address

			})
	else:
		form = ExaminerDriverInformationForm({
				'first_name': driver.first_name,
				'last_name': driver.last_name,
				'middle_initial': driver.middle_initial,
				'date_of_birth': driver.date_of_birth,
				'gender': driver.gender,
				'street_address': address.street_address,
				'city': address.city,
				'state': address.state,
				'zip_code': address.zip_code,
				'driver_license_number': license.number,
				'issuing_state': license.issuing_state,
				'phone_number': driver.phone_number,
				'email_address': driver.email_address

			})
	return render(request, 'examiner_driver_history.html', \
		{'form':form, 'driver':driver})

@login_required(login_url='/examiner/login/')
def driver_search(request):
	'''
	Server side component to ajax search.
	'''
	if request.method == 'POST':
		queries = request.POST['search_text'].split()
		# allows for better searching of first and last name but still could
		# be improved
		qset = reduce(operator.__or__, [(Q(first_name__icontains=query) & Q(examiner_id=request.user.id))| \
		(Q(last_name__icontains=query) & Q(examiner_id=request.user.id)) for query in queries])
	else:
		qset = ''

	drivers = Driver.objects.filter(qset).order_by('first_name')
	html = ''
	for driver in drivers:
		html += '''<tr class="driver-page" id="{}" data-href='/examiner/{}/driver/{}'>
				<td scope="row"></td> 
				<td scope="row" name="{}">{}</td> 
				<td>{}</td><td>{}</td><td>{}</td><td class="examiner-begin-exam"><a href='/examiner/{}/driver/{}/exam/'>Begin Exam</a></td></tr>'''.format(driver.id,request.user.id, 
						driver.id,driver.id,
						driver.first_name,driver.last_name,driver.date_of_birth,
						driver.registration_date, request.user.id, driver.id)
	if html != '' :
		return HttpResponse(html)


@login_required(login_url='/examiner/login/')
def driver_clear_search(request):
	'''
	Returns all drivers when the form is cleared by the user
	'''
	if request.method == 'POST':
		drivers = Driver.objects.filter(examiner_id=request.user.id).order_by('first_name')
		html = ''
		for driver in drivers:
			html += '''<tr class="driver-page" id="{}" data-href='/examiner/{}/driver/{}'>
					<td scope="row"></td> 
					<td scope="row" name="{}">{}</td>
					<td>{}</td><td>{}</td><td>{}</td><td class="examiner-begin-exam"><a href='/examiner/{}/driver/{}/exam/'>Begin Exam</a></td></tr>'''.format(driver.id,request.user.id, 
						driver.id,driver.id,
						driver.first_name,driver.last_name,driver.date_of_birth,
						driver.registration_date, request.user.id, driver.id)
		if html != '' :
			return HttpResponse(html)






    # render_to_response('driver_search.html', \
        # {'results' : results})
	# first_name = forms.CharField() 
	# last_name = forms.CharField() 
	# middle_initial = forms.CharField()
	# date_of_birth = forms.CharField()
	# gender = forms.ChoiceField(choices=GENDER)

	# # address information
	# street_address = forms.CharField()
	# city = forms.CharField() 
	# state = forms.ChoiceField(choices=STATES) 
	# zip_code = forms.CharField()	
	
	# # driver license information
	# driver_license_number = forms.CharField()
	# issuing_state = forms.ChoiceField(choices=STATES)	

	# # contact information
	# phone_number = forms.CharField()
	# email_address = forms.CharField(label="E





# IDEA
# Scrape site that lists all CME and get their email addresses
# Allow drivers to request that their CME use our software

# unused exam forms
	# examquestionsform = ExamQuestionsForm() 
	# bloodpressureform = BloodPressureForm() 
	# urinalysisform = UrinalysisForm() 
	# visionform = VisionForm() 
	# hearingform = HearingForm() 
	# physicalexamform = PhysicalExamForm() 
	# examdeterminationform = ExamDeterminationForm()
		# {
		# 'examquestionsform':examquestionsform,
		# 'bloodpressureform':bloodpressureform,
		# 'urinalysisform':urinalysisform,
		# 'visionform':visionform,
		# 'hearingform':hearingform,
		# 'physicalexamform':physicalexamform,
		# 'examdeterminationform':examdeterminationform,
		# }


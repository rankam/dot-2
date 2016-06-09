from drivers.models import Driver



# id = models.AutoField(primary_key=True)
# 	last_name = models.CharField(max_length=200)
# 	first_name = models.CharField(max_length=200)
# 	middle_initial = models.CharField(max_length=10)
# 	email_address = models.EmailField(null=True)
# 	date_of_birth = models.DateField(max_length=8)
# 	phone_number = models.CharField(max_length=10)
# 	gender = models.CharField(max_length=10, choices=GENDERS, default=MALE)
# 	registration_date = models.DateTimeField(auto_now=True)
# 	examiner = models.ForeignKey(Examiner)

# def fake_drivers(examiner_id=None):
# 	
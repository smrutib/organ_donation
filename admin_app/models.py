from django.db import models
class Heart_Waitlist(models.Model):
	hos_name = models.CharField(max_length=100)
	patient_id = models.CharField(max_length =5, primary_key=True)
	p_name = models.CharField(max_length=75)
	pri_choices = (
		('1a','1a'),
		('1b','1b'),
		('2','2')
	)
	priority = models.CharField( max_length=2 , choices=pri_choices, default='2')
	status_choices =(
		('I','Inactive'),
		('A','Active')
		)
	status = models.CharField( max_length=1 , choices=status_choices, default='A' )
	age = models.IntegerField()
	height = models.IntegerField()
	weight = models.IntegerField()
	blood_choices =(
		('A+','A+'),
		('A-','A-'),
		('B+','B+'),
		('B-','B-'),
		('AB+','AB+'),
		('AB-','AB-'),
		('O+','O+'),
		('O-','O-'),
		)
	blood_type = models.CharField(max_length=3, choices=blood_choices)

class Heart_Donor(models.Model):
	donor_id = models.CharField(max_length =5, primary_key=True)
	d_name = models.CharField(max_length=75)
	age = models.IntegerField()
	height = models.IntegerField()
	weight = models.IntegerField()
	blood_choices =(
		('A+','A+'),
		('A-','A-'),
		('B+','B+'),
		('B-','B-'),
		('AB+','AB+'),
		('AB-','AB-'),
		('O+','O+'),
		('O-','O-'),
		)
	blood_type = models.CharField(max_length=3, choices=blood_choices)

class Liver_Donor(models.Model):
	donor_id = models.CharField(max_length =5, primary_key=True)
	d_name = models.CharField(max_length=75)
	age = models.IntegerField()
	blood_choices =(
		('A+','A+'),
		('A-','A-'),
		('B+','B+'),
		('B-','B-'),
		('AB+','AB+'),
		('AB-','AB-'),
		('O+','O+'),
		('O-','O-'),
		)
	blood_type = models.CharField(max_length=3, choices=blood_choices)

class Liver_Waitlist(models.Model):
	hos_name = models.CharField(max_length=100)
	patient_id = models.CharField(max_length =5, primary_key=True)
	p_name = models.CharField(max_length=75)
	status_choices =(
		('I','Inactive'),
		('A','Active')
		)
	status = models.CharField( max_length=1 , choices=status_choices, default='A' )
	age = models.IntegerField()
	blood_choices =(
		('A+','A+'),
		('A-','A-'),
		('B+','B+'),
		('B-','B-'),
		('AB+','AB+'),
		('AB-','AB-'),
		('O+','O+'),
		('O-','O-'),
		)
	blood_type = models.CharField(max_length=3, choices=blood_choices)
	MELD=models.IntegerField()

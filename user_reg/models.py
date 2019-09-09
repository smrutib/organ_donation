from django.db import models

class FormModel(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=50)
	contact=models.CharField(max_length=10)
	weight = models.DecimalField(decimal_places=2, max_digits=4)
	height = models.DecimalField(decimal_places=2, max_digits=4)
	address=models.CharField(max_length=200)
	country=models.CharField(max_length=200)
	state=models.CharField(max_length=200)
	city=models.CharField(max_length=200)
	zipCode=models.CharField(max_length=6)
	GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
   )
	gender = models.CharField(choices=GENDER_CHOICES,max_length=10)


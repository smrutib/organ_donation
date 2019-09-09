
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
	# add additional fields in here
	name=models.CharField(max_length=256)
	username=models.CharField( max_length=100,primary_key=True)
	password=models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	telephone=models.CharField(max_length=10)
	zip_code = models.CharField(max_length=20)
	state = models.CharField(max_length=100)
	country = models.CharField(max_length=100)

	def __str__(self):
		return self.name
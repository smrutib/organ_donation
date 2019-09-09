from django.forms import ModelForm
from admin_app.models import Heart_Waitlist
from admin_app.models import Heart_Donor

class HeartWaitlistForm(ModelForm):
	class Meta:
		model = Heart_Waitlist
		fields = '__all__'

class HeartDonorForm(ModelForm):
	class Meta:
		model = Heart_Donor
		fields = '__all__'

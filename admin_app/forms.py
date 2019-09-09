from django.forms import ModelForm
from admin_app.models import Heart_Waitlist,Liver_Waitlist,Kidney_Waitlist
from admin_app.models import Heart_Donor,Liver_Donor,Kidney_Donor

class HeartWaitlistForm(ModelForm):
	class Meta:
		model = Heart_Waitlist
		fields = '__all__'

class HeartDonorForm(ModelForm):
	class Meta:
		model = Heart_Donor
		fields = '__all__'


class KidneyWaitlistForm(ModelForm):
	class Meta:
		model = Kidney_Waitlist
		fields = '__all__'

class KidneyDonorForm(ModelForm):
	class Meta:
		model = Kidney_Donor
		fields = '__all__'

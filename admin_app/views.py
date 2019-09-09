from django.shortcuts import render
from django.http import HttpResponse
from . import forms

def index(request):
	return render(request,'admin_app/index.html')
def waitlist(request):
	if request.method == 'POST':
		form = forms.HeartWaitlistForm(request.POST)
		if form.is_valid():
			record =form.save()
			record.save()
			form = forms.HeartWaitlistForm()
	else:
		form = forms.HeartWaitlistForm()
	return render(request,'admin_app/waitlist.html',{'form':form})
def donor(request):
	if request.method == 'POST':
		form = forms.HeartDonorForm(request.POST)
		if form.is_valid():
			record =form.save()
			record.save()
			form = forms.HeartDonorForm()
	else:
		form = forms.HeartDonorForm()
	return render(request,'admin_app/donor.html',{'form':form})
def check(request):
	return render(request,'admin_app/check.html')
# Create your views here.


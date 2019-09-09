from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
	return render(request,'user_reg/index.html')

def form_name_view(request):
	form=forms.FormName()
	return render(request,'user_reg/user_reg.html',{'form':form})



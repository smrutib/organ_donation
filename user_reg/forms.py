from django import forms
from user_reg.models import FormModel
class FormName(forms.ModelForm):
	#address=forms.CharField(widget=forms.Textarea)
	#gender=forms.ChoiceField(widget=forms.RadioSelect())
	class Meta:
		model=FormModel
		fields='__all__'


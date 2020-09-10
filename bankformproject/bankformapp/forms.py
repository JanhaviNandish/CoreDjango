from django import forms
from . models import BankForm

class AccRegistration(forms.ModelForm):
	class Meta:
		model = BankForm
		fields = '__all__'
    
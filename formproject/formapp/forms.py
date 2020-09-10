from django import forms

class StudentRegistration(forms.Form):
	NAME = forms.CharField()
	MARKS = forms.IntegerField()
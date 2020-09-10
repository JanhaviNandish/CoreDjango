from django import forms
from .models import UploadingImage

class DisneyForm(forms.ModelForm):
    # TODO: Define form fields here

    class Meta:
    	model = UploadingImage
    	fields = '__all__'

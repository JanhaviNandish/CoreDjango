from django.shortcuts import render
from .models import UploadingImage
from .forms import DisneyForm
from django.http import HttpResponse

# Create your views here.
def disnimgview(request):
	form = DisneyForm()
	if request.method=='POST':
		form = DisneyForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return success(request)
	return render(request,'imageapp/display.html',{'form':form})

def success(request):
	s1 = "<center><h1>Image was Sucessfully Uploaded</h1></center>"
	return HttpResponse(s1)


def display_disn_img(request):
	if request.method=='GET':
		disneypic = UploadingImage.objects.all()
		return render(request,'imageapp/image.html',{'disneypic':disneypic})


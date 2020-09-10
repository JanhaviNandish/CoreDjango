from django.shortcuts import render
from .forms import AccRegistration
from django.http import HttpResponse

# Create your views here.
def accregisterview(request):
	form = AccRegistration()
	if request.method=='POST':
		form = AccRegistration(request.POST)
		if form.is_valid():
			form.save()
			print('Data got inserted into Database successfully')
			return success(request)
	return render(request,'bankformapp/display.html',{'form':form})

def success(request):
	s1 = "<center><h1>Account details uploaded successfully</h1></center>"
	return HttpResponse(s1)
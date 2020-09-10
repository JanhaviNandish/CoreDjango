from django.shortcuts import render

# Create your views here.
def switzerland(request):
	msg = "works in switzerland"
	my_dict = {'msg':msg}

	return render(request,'countryapp/display2.html',context=my_dict)

def newzeland(request):
	msg = "works in newzeland"
	my_dict = {'msg':msg}

	return render(request,'countryapp/display2.html',context=my_dict)
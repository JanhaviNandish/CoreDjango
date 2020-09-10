from django.shortcuts import render

# Create your views here.

def uc_1(request):
	msg = "JAVA AND TESTING"
	my_dict = {'msg':msg}

	return render(request,'courseapp/display3.html',context=my_dict)


def uc_2(request):
	msg = "PYTHON AND TESTING"
	my_dict = {'msg':msg}

	return render(request,'courseapp/display3.html',context=my_dict)


def uc_3(request):
	msg = "JAVA, TESTING AND PYTHON"
	my_dict = {'msg':msg}

	return render(request,'courseapp/display3.html',context=my_dict)

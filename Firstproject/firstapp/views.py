from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome_django(request):
	s1="<h1>hello everyone</h1>"
	s2="<h1>This is my first project in django</h1>"
	s3=(s1,s2)
	return HttpResponse(s3)
from django.shortcuts import render
from .models import Student_Info
# Create your views here.

def display_student(request):
	student_lst = Student_Info.objects.all()

	return render(request,'studentinfoapp/display.html',{'student':student_lst})
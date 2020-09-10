from django.shortcuts import render
from datetime import datetime

# Create your views here.
def greet_dhoni(request):
	date = datetime.now()
	time = int(date.strftime('%H'))
	msg1 = "We Wish You Very HAPPY BIRTHDAY DHONI..."

	if time<12:
		msg = "Good Morning"

	elif time<16:
		msg = "Good Afternoon"

	elif time<20:
		msg = "Good Evening"

	else:
		msg = "Good Night"

	my_dict = {'msg': msg, 'msg1':msg1,'date':date}

	return render(request,'sixthapp/display.html',context=my_dict)
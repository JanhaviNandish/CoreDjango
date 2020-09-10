from django.contrib import admin
from .models import Student_Info
# Register your models here.

class Student_InfoAdmin(admin.ModelAdmin):

	list_display=('FIRSTNAME','LASTNAME','CLGNAME','BRANCH','DOB','GENDER','DEPT','STUDENT_ID')

admin.site.register(Student_Info,Student_InfoAdmin)
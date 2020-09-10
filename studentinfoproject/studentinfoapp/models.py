from django.db import models

# Create your models here.
class Student_Info(models.Model):
	FIRSTNAME = models.CharField(max_length=50)
	LASTNAME = models.CharField(max_length=50)
	CLGNAME = models.CharField(max_length=50)
	BRANCH = models.CharField(max_length=50)
	DOB = models.DateField()
	GENDER = models.CharField(max_length=50)
	DEPT = models.CharField(max_length=50)
	STUDENT_ID = models.CharField(max_length=50)

	class Meta:
		verbose_name = "Student_Info"
		verbose_name_plural = "Student_Infos"

		def __str__(self):
			pass
    
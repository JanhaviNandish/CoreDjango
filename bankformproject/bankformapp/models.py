from django.db import models

# Create your models here.
class BankForm(models.Model):
	NAME = models.CharField(max_length=50)
	AGE = models.IntegerField()
	DOB = models.DateField()
	ADDRESS = models.CharField(max_length=50)
	ACCTYPE = models.CharField(max_length=50)
	BRANCH = models.CharField(max_length=50)
	EMAIL = models.EmailField()
	AADHARNO = models.IntegerField()



	class Meta:
		verbose_name = "BankForm"
		verbose_name_plural = "BankForms"

		def __str__(self):
			pass
    
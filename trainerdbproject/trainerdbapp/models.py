from django.db import models

# Create your models here.
class Trainer_Info(models.Model):
	FIRSTNAME = models.CharField(max_length=50)
	LASTNAME = models.CharField(max_length=50)
	DOMAIN = models.CharField(max_length=50)
	EXPERIENCE = models.IntegerField()
	BRANCH  = models.CharField(max_length=50)
	ADDRESS  = models.CharField(max_length=50)
	NO_OF_BATCHES = models.IntegerField()
	SALARY = models.IntegerField()
	
	class Meta:
		verbose_name = "Trainer_Info"
		verbose_name_plural = "Trainer_Infos"

		def __str__(self):
			pass


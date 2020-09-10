from django.db import models

# Create your models here.
class Movie_Info(models.Model):
	HERO_NAME = models.CharField(max_length=50)
	HEROINE_NAME = models.CharField(max_length=50)
	MOVIE_NAME = models.CharField(max_length=50)
	RELEASE_DATE = models.DateField()
	MOVIE_DURATION =models.FloatField()
	NO_OF_SONGS = models.IntegerField()

	class Meta:
		verbose_name='Movie_Info'
		verbose_name_plural='Movie_Infos'

		def __str__(self):
			pass


	
		
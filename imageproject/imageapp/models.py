from django.db import models

# Create your models here.
class UploadingImage(models.Model):
	Name = models.CharField(max_length=50)
	image = models.ImageField(upload_to = 'images/')


	class Meta:
		verbose_name = "UploadingImage"
		verbose_name_plural = "UploadingImages"


		def __str__(self):
			pass


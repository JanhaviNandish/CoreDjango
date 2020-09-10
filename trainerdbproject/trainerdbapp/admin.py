from django.contrib import admin
from . models import Trainer_Info

# Register your models here.
class Trainer_InfoAdmin(admin.ModelAdmin):
	list_display = ('FIRSTNAME','LASTNAME','DOMAIN','EXPERIENCE','BRANCH','ADDRESS','NO_OF_BATCHES','SALARY')

admin.site.register(Trainer_Info,Trainer_InfoAdmin)
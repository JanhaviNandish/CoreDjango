
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('fb/',views.facebook),
	path('wtsup/',views.whatsapp),
	path('insta/',views.instagram),
]
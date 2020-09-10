"""eighthproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bankapp import views as v1
from countryapp import views as v2
from courseapp import views as v3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('depo/',v1.deposit),
    path('bal/',v1.balance),
    path('draw/',v1.withdraw),
    path('swizz/',v2.switzerland),
    path('newze/',v2.newzeland),
    path('uc1/',v3.uc_1),
    path('uc2/',v3.uc_2),
    path('uc3/',v3.uc_3),
]

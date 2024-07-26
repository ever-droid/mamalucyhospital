
from django.contrib import admin
from django.urls import path
from MamaLucyHospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='home'),
    path('inner/', views.inner, name='inner'),
    path('about/', views.about, name='about'),
    path('doctors/', views.doctors, name='doctors'),
    path('appointment/', views.appointment, name='appointment'),
]

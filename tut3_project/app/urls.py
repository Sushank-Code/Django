from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
   path('', views.index, name='home'),
   path('contact/',views.contact,name='contact')
]

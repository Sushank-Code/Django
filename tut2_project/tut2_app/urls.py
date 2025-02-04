from django.contrib import admin
from django.urls import path
from tut2_app import views as vap

urlpatterns = [
    path('', vap.index, name='Home'),
    path('about/', vap.about, name='About'),
    path('math/', vap.math, name='Math')
]

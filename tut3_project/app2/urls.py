from django.contrib import admin
from django.urls import path
from app2 import views

urlpatterns = [
   path('about/', views.about, name='About'),
   path('filter/', views.demofilter, name='Filter'),
]

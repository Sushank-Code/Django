from django.contrib import admin
from django.urls import path
from tut2_app2.views import about2

urlpatterns = [
    path('about2/', about2,{'status':'ok'},name='About'),
    path('about2.0/', about2, name='About'),
]

from django.contrib import admin
from django.urls import path
from home import views

 
urlpatterns = [
    path("",views.index,name='home'),
    path("about/",views.about,name='about'),
    path("contact/",views.contact,name='contact'),
    path("registration/",views.registration,name='registration'),
    path("login/",views.login,name='login'),
    path("demoform/",views.demoform,name='demoform'),
    path("modelform/",views.ModelForm,name='modelform'),
    path("modelcontact/",views.ModelContact,name='modelcontact'),
    path("messages/",views.Msgframework,name='messages'),
]

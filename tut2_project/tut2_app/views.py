from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.

def index(request): 
    return HttpResponse("Home page")
   

def about(request):
    return HttpResponse("<h1>About page</h1>")

def math(request):
    a = 10 + 10
    return HttpResponse(a)
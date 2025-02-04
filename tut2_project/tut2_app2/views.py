from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.

def about2(request,**kwargs):
    status =kwargs.get('status','No bro')
    return HttpResponse(f"<h1>About page2 {status}</h1>")
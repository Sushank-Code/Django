from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    #return HttpResponse("Hello world !")
    messages.success(request,"This is a test message")
    return render(request,'index.html')

def about(request):
    #return HttpResponse("This is about page")
    return render(request,'about.html')

def contact(request):
   #return HttpResponse("This is contact page")
    if(request.method == "POST"):
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,contact=contact,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent ! ")
    return render(request,'contact.html')


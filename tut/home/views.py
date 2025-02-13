from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from django.contrib import messages
from home.models import Contact,Login   
from home.forms import Registration,Loginf,DemoForm

# Create your views here.
def index(request):
    # messages.success(request,"This is a test message")
    return render(request,'home/index.html')

def about(request):
    contact_data = Contact.objects.all()
    contact_data2 = Contact.objects.first()    # For single data (single Object)
    context ={
        'contact_data' : contact_data,
        'contact_data2' : contact_data2,
    }
    return render(request,'home/about.html',context) 

def contact(request):                     # Yo Html Form ho Django ko form hoina
    if(request.method == "POST"):
        name=request.POST.get('name')
        email=request.POST.get('email')  
        contact=request.POST.get('contact')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,contact=contact,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent ! ")
    return render(request,'home/contact.html') 

def registration(request):
    fm = Registration()
    fm2 = Loginf()
    # fm = Registration(auto_id=True)
    # fm = Registration(auto_id=False)
    # fm = Registration(auto_id='sushank_%s')

    # fm = Registration(label_suffix="A",initial={
    #     'email':'Enter a email',
    #     'first_name': 'FirstName',
    # })

    context = {
        'form': fm,
        'login': fm2,
    }
    return render(request,'home/registration.html',context)   

def demoform(request):
    demoform = DemoForm()
    
    return render(request,'home/demoform.html',{'demoform':demoform})   

def login(request):            
    if(request.method == "POST"):   
        login = Loginf(request.POST)    # for post request
        if login.is_valid():
            nm = login.cleaned_data['name']
            em = login.cleaned_data['email']
            passw = login.cleaned_data['password']
            user = Login(name=nm,email=em,password= passw)
            user.save()
            return redirect('/login/')
    else:
        login = Loginf()          # for get request
    return render(request,'home/login.html',{'login':login})     
from django.shortcuts import render,HttpResponse,redirect
from home.forms import Registration,Loginf,DemoForm,SignForm,ModelContact2
from home.models import Contact,Login,Contact2
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    # messages.success(request,"This is a test message")
    return render(request,'home/index.html')

def about(request):
    contact_data = Contact.objects.all()
    contact_data2 = Contact.objects.first()     # For single data (single Object)
    context = {
        'contact_data' : contact_data,
        'contact_data2' : contact_data2,
    }
    return render(request,'home/about.html',context) 

def contact(request):                     # Yo custom Html Form ho Django ko form hoina
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
        login = Loginf()                                  # for get request
    return render(request,'home/login.html',{'login':login})     

def ModelForm(request):
    if(request.method == "POST"):                       # for post request 
        mf = SignForm(request.POST)    
        if mf.is_valid():
            mf.save()
            return redirect('/modelform/')
    else:
        mf = SignForm()                                  # for get request
    return render(request,'home/modelform.html',{'modelform': mf})     

def ModelContact(request):
    if(request.method == "POST"):                   
        cf2 = ModelContact2(request.POST)    
        if cf2.is_valid():
            cf2.save()
            return redirect('/modelcontact/')
    else:
        cf2 = ModelContact2()
    return render(request,'home/modelcontact.html',{'contact2':cf2})     

def Msgframework(request):
    # messages.add_message(request,messages.SUCCESS,"Your message")

    messages.success(request,"Sucess Message")
    messages.warning(request,"Warning message")
    messages.error(request,"Error Message")
    return render(request,'home/msg.html')      
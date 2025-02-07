from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    version = 5.1
    course = {'Name': 'Django',
              'version': version,
              'click':'click me',
              'click2':'SIGN IN',
              'click3':'log in hello',
              'click4':'jijjoasdaskjdhaskhdjaskdh',
              'Date':datetime.now(),
              'floatnum':51.89888898213,
              'alert':True,
              'danger':"Notification",
            }
    card ={
        'cardname1' : 'Ecommerse',
        'cardname2' : 'Blog',
        'cardname3' : 'Video',
    }
    context = {'course': course, 'card': card}       # 2 dictionary or more
    # return render(request,'app/index.html',context=course) # 1st approach
    # return render(request,'app/index.html',course)         # 2nd approach
    # return render(request,'app/index.html',context={'Name': 'Django2.0'}) # 3rd approach
    return render(request,'app/index.html',context)
    
def contact(request):
    return render(request,'app/contact.html')
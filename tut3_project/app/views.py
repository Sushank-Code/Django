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
              'floatnum':51.89888898213
            }
    # return render(request,'app/index.html',context=course)
    # return render(request,'app/index.html',context={'Name': 'Django2.0'})
    return render(request,'app/index.html',course)

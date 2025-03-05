from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'app2/about.html')

def demofilter(request):
    data ={'About': " Hello, I am learning Django"
    
    }
    
    return render(request,'app2/demofilter.html',data)
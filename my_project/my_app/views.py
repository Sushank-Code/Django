from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login

# password = lamsal123**
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def loginuser(request):
    if(request.method == "POST"):
        username =   request.POST.get('username')
        password =   request.POST.get('password')
        user=authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request,'login.html')
        
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")

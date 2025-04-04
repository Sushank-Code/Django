from django.shortcuts import render,redirect,HttpResponse
from custom_authapp.forms import RegistrationForm
from django.contrib import messages  
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.
def home(request):
    return render(request,'custom_authapp/home.html')

def login_view(request):
    return render(request,'custom_authapp/login.html')

def register_view(request):
    
    if request.method == "POST":
        rf = RegistrationForm(request.POST)
        if rf.is_valid():
            user = rf.save(commit=False)
            user.set_password(rf.cleaned_data['password']) # hash the password
            user.is_active = False   # user can't login until activation(via: email or admin)
            user.save()
            messages.success(request," Success! Please Check Your email for activation")
            return redirect('Login')
    else:
        rf = RegistrationForm()
    return render(request,'custom_authapp/registration.html',{'rform':rf})

def send_test_email(request):
    subject = 'Test Email'
    html_message = render_to_string('custom_authapp/activation_email.html')
    # plain_message = 'This is Plain text'
    from_email ='admin@example.com'
    to_email = ['user@example.com']

    email = EmailMessage(
        subject = subject,
        body = html_message,
        from_email=from_email,
        to=to_email
    )
    email.content_subtype = 'html'  # set the email type
    email.send()
    return HttpResponse("Test email send")

def password_reset_view(request):
    return render(request,'custom_authapp/password_reset.html')

def password_reset_confirm_view(request):
    return render(request,'custom_authapp/password_reset_confirm.html')
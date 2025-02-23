import re
from django import forms
from home.models import Login,Contact2
from django.core.validators import MaxLengthValidator,MinLengthValidator,EmailValidator
from django.core.exceptions import ValidationError
# Creating Forms
  
class Registration(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


STRICT_EMAIL_REGEX =  r'^[a-zA-Z0-9._%+-]+@(gmail\.com|yahoo\.com)$' 
def strict_email_validator(value):
    if not re.match(STRICT_EMAIL_REGEX , value):
        raise ValidationError("Please enter a valid email address.")
    
class Loginf(forms.Form):
    name = forms.CharField(label="Name",
                           validators=[MinLengthValidator(3),MaxLengthValidator(10)],
                            widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}) ,
                           )
    email= forms.CharField(
                            label="Email",
                            widget=forms.EmailInput(attrs={'placeholder': 'example@gmail.com'}) ,
                            validators=[strict_email_validator],
                        )
    password = forms.CharField(label="Password",
                                widget=forms.PasswordInput)

class DemoForm(forms.Form):
    name = forms.CharField(max_length=100,
                            label="FullName",
                            # initial="Enter fullname",
                            # validators=[MinLengthValidator(3)],
                            min_length=3,
                            widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}) ,
                            )
    
    email = forms.EmailField(max_length=25,
                            label="Email",
                            widget=forms.EmailInput(attrs={'placeholder': 'example@gmail.com'}) ,
                            )
    
    choices = [('M','Male'),
                ('F','Female'),
            ]
    gender= forms.ChoiceField(label='Choose a Gender', choices=choices, required=False)
                            
    #  = forms.MultipleChoiceField(, choices=[CHOICES], required=False)

    is_logged = forms.BooleanField(label="Is logged", required=False)

    terms = forms.NullBooleanField(label="Do you agree the terms ", required=False)
                           
    date = forms.DateField(label="Date",
                            widget=forms.DateInput(attrs={'type':'date', }) ,
    )  

    time = forms.TimeField(label="Time",
                            widget=forms.TimeInput(attrs={'type':'time', }) ,
    )  
    
    post_content = forms.CharField(label="Textarea", 
                                   widget=forms.Textarea(attrs={'placeholder':'Write something here'}, )
    )
    file = forms.FileField(label="upload",
                           widget=forms.FileInput())
    
# Model form

class SignForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ["name","email","password"] 

class ModelContact2(forms.ModelForm):
    class Meta:
        model = Contact2
        fields = "__all__"
        
    email = forms.EmailField(
        required=True,
        validators=[strict_email_validator],  
    )
    
    
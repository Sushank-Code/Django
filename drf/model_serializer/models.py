import re
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

STRICT_EMAIL_REGEX =  r'^[a-zA-Z0-9._%+-]+@(gmail\.com|yahoo\.com)$' 
def strict_email_validator(value):
    if not re.match(STRICT_EMAIL_REGEX , value):
        raise ValidationError("Please enter a valid email address.")

class Info(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=20,unique=True,validators=[strict_email_validator])
    
    choices =[('M','Male'),
              ('F','Female'),
            ] 
    gender = models.CharField(max_length=20,choices = choices)


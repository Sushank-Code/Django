from django import forms
from custom_authapp.models import User
from django.core.exceptions import ValidationError


class RegistrationForm(forms.ModelForm):
    
    password = forms.CharField(widget = forms.PasswordInput)
    confirm_password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ["name","email","password","confirm_password"]

    # checking password and confirm password same or not
    def clean(self):  # clean is used for multiple validation
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        # print("p :",password)
        # print("cp :",confirm_password)
        
        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password","Password and confirm password are not matching!")
        return cleaned_data

    def clean_email(self):   # clean_'fieldname' is used for singel validation
        email = self.cleaned_data.get("email")
        if User.objects.filter(email = email).exists():
            raise ValidationError("Email already exists")
        return email
            
            
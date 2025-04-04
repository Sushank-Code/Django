from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
 
# Create your models here.

class UserManager(BaseUserManager):

    # Create a normal User 
    def create_user(self,email,password=None):
        # create and save an User with the given email and password
        if not email:
            raise ValueError("User must have an valid email address")
        
        # Normalize the email (e.g., converting uppercase to lowercase)
        user = self.model(email=self.normalize_email(email))

         # Set and hash the password
        user.set_password(password)

        # Save the user to the database
        user.save(using=self.db)
        return user
    
    # Create a super user
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
    
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.is_customer = True
        user.is_seller = True
        user.save(using=self.db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=254,unique=True)
    name = models.CharField(max_length=254)
    city = models.CharField(max_length=254,blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)
    is_seller = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = "email"
    
    objects = UserManager()

    def __str__(self):
        return self.email
    
from django.db import models

# Create your models here.
class Contact(models.Model):
    name =models.CharField(max_length=122)
    email =models.CharField(max_length=122)
    contact =models.CharField(max_length=15)
    desc = models.TextField()
    date = models.DateField()

    # def __str__(self):
    #     return self.name 

class student(models.Model):
    name =models.CharField(max_length=122)
    age = models.IntegerField()

class Login(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=120)
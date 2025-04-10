from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20,unique=True)
    phone = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
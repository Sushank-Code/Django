from django.contrib import admin
from home.models import Contact,student,Login,Contact2

# Register your models here.

# admin.site.register(Contact)   # First method

class ContactAdmin(admin.ModelAdmin): # 2nd Method
    list_display = ('id','name','email','contact','date')

admin.site.register(Contact,ContactAdmin)

# Other method using decorator

@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display = ('id','name','age')

@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','password')

@admin.register(Contact2)
class Contact2Admin(admin.ModelAdmin):
    list_display = ('id','name','email')
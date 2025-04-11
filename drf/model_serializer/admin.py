from django.contrib import admin
from model_serializer.models import Info

# Register your models here.
@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('id','username','email','gender')
    list_display_links = ('id',)
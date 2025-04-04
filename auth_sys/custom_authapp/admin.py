from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from custom_authapp.models import User

# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['id','email','name','is_active','is_staff','is_superuser','is_customer',    'is_seller']
    list_display_links = ['email']
    list_filter = ['is_superuser']

    # Fields to display when editing/viewing a user in admin
    fieldsets = (
        ("User Credentials", {
            "fields": (
                'email','password'
            ),
        }),
        ("Personal Info", {
            "fields": (
                'name','city',
            ),
        }),
        ("Permissions", {
            "fields": (
                'is_active','is_staff','is_superuser','is_customer','is_seller'
            ),
        }), 
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email","password1", "password2"),
        }),
    )

    search_fields =['email']
    ordering = ['email','id']
    filter_horizontal = []

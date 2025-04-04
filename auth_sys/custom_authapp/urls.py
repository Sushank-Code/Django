from django.urls import path
from custom_authapp import views

urlpatterns = [
    path('',views.home,name='Home'),
    path('login/',views.login_view,name='Login'),
    path('registration/',views.register_view,name='Registration'),
    path('password_reset/',views.password_reset_view,name='Passwordreset'),
    path('password_reset_confirm/',views.password_reset_confirm_view,name='Passwordresetconfirm'),
    path('send_email/',views.send_test_email,name='Sendemail'),
]
 
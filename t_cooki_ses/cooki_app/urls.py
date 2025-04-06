from django.urls import path
from cooki_app import views

urlpatterns = [
    path('setcookie/',views.setcookie,name='setcookie'),
    path('getcookie/',views.getcookie,name='getcookie'),
    path('delcookie/',views.delcookie,name='delcookie'),
    path('setsession/',views.setsession,name='setsession'),
    path('getsession/',views.getsession,name='getsession'),
    path('delsession/',views.delsession,name='delsession'),
    path('flush/',views.flushsession,name='flushsession'),
]

from django.urls import path,include
from model_serializer import views

urlpatterns = [
    path('model_info/',views.Info_create)
]
from django.urls import path,include
from api import views

urlpatterns = [
    path('api/<int:pk>', views.contact_view),
    path('api_all/', views.contact_view_all),
]
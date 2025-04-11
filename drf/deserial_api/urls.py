from django.urls import path,include
from deserial_api import views

urlpatterns = [
    path('stu_create/',views.student_create)
]
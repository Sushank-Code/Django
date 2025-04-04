from django.urls import path
from customer import views

urlpatterns = [
    path('customer_dashboard/',views.customer_dashboard_view,name='Customerdash'), 
    path('password_change/',views.password_change_view,name='Passchange'), 
]  
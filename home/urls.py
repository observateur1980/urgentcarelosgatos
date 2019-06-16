
from django.urls import path
from  . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'home'
urlpatterns = [
    
    
    path('', views.Home.as_view(), name='home'),
    path('billing', views.Billing.as_view(), name='billing'),
    path('services', views.Services.as_view(), name='services'),
    path('facilty', views.Facilty.as_view(), name='facilty'),
    path('contact', views.Contact.as_view(), name='contact'),
    path('blog', views.Blog.as_view(), name='blog'),
    path('sending_email', views.sending_email, name='sending_email'),
    path('make_appointment', views.make_appointment, name='make_appointment'),
    path('make_appointment_home', views.make_appointment_home, name='make_appointment_home'),
    
    
   
]

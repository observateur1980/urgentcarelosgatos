
from django.urls import path
from  . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'home'
urlpatterns = [
    
    
    path('', views.Home.as_view(), name='home'),
    # path('about', views.About.as_view(), name='about'),
    # path('services', views.Services.as_view(), name='services'),
    # path('events', views.Events.as_view(), name='events'),
    path('contact', views.Contact.as_view(), name='contact'),
    path('sending_email', views.sending_email, name='sending_email'),
    path('make_appointment', views.make_appointment, name='make_appointment'),
    
    
   
]

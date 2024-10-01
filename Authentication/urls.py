from django.urls import path
from . import views

urlpatterns = [
    path ('userregistration/', views.register, name='register')
    
]
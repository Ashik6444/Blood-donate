from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.Register, name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('pst',views.pst,name='pst'),
    path('donate',views.donates,name='donate')
    
    

    
]

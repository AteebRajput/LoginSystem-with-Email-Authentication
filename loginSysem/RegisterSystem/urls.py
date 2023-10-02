from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('home',views.home,name='home'),
    path('login',views.loginpage,name='login'),
    path('register',views.register,name='register'),
    path('signout',views.signout,name='signout'),

]
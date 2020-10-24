from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('search', views.search, name='search'),
    path('write', views.write, name='write'),
    path('feedback', views.feedback, name='feedback'),
    path('signup', views.signup, name='signup'),
    path('login', views.handellogin, name='handellogin'),
    path('login', views.login, name='login'),
    path('logout', views.handellogout, name='handellogout'),
    path('profile', views.profile, name='profile'),
]
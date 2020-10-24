from django.contrib import admin
from django.urls import path, include
from blog import views
urlpatterns = [
    
    #API to post a comment
    path('blogComment', views.blogComment, name='blogComment' ),
    path('', views.bloghome, name='bloghome'),
    path('<str:slug>', views.blogpost, name='blogpost'),
    
]
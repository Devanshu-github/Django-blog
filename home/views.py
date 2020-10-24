# Create your views here.
from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from home.models import Contact, Feedback
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from blog.models import Post
from math import ceil
import datetime
import random
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

def search(request):
    search = request.GET['search']
    str(search)
    if len(search)>50:
        allpost = Post.objects.none()
    else:
        allposttitle = Post.objects.filter(title__icontains=search)
        allpostcontent = Post.objects.filter(content__icontains=search)
        allpostname = Post.objects.filter(name__icontains=search)
        allpostcategories = Post.objects.filter(Categories__icontains=search)
        allpost = allposttitle.union(allpostname, allpostcontent, allpostcategories)
    if allpost.count()==0:
        messages.error(request, "No search result found please refine your query" )
    params = {'allpost':allpost, 'search':search}
    return render(request, 'home/search.html', params)

# Create your views here.
def home(request):
    print(User) #-1 0 1 2 3
    if request.user.is_authenticated:
        posts = Post.objects.all()[::-1]
        context = {'posts':posts}
    else:
        posts = Post.objects.all()[:4]
        context = {'posts':posts}
    return render(request, 'home/index.html', context)

def about(request): 
    return render(request, 'home/about.html')

with open("user.txt", "r") as f:
    a = f.read()
Unames = [i for i in a]



def contact(request):
    messages.info(request, "Have any Query/Message? Fill Details bellow to Contact Us")
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        categories = request.POST['categories']
        message = request.POST['message']
        # print(name, email, categories, message)
        if len(str(name))<2 or len(str(email))<10 or len(str(messages))<10:
            messages.error(request, "Please fill the form Correctly")
        else:
            contact = Contact(name=name, email=email, categories=categories, message=message)
            contact.save()
            send_mail(
            'Message from: ' + name,
            message,
            email,
            ['quaintvisionweb@gmail.com'],
             fail_silently=False,
            )
            messages.success(request, "Message Sent Successfully!")
    return render(request, 'home/contact.html')

def search(request):
    search = request.GET['search']
    str(search)
    if len(search)>50:
        allpost = Post.objects.none()
    else:
        allposttitle = Post.objects.filter(title__icontains=search)
        allpostcontent = Post.objects.filter(content__icontains=search)
        allpostname = Post.objects.filter(name__icontains=search)
        allpostcategories = Post.objects.filter(Categories__icontains=search)
        allpost = allposttitle.union(allpostname, allpostcontent, allpostcategories)
    if allpost.count()==0:
        messages.error(request, "No search result found please refine your query" )
    params = {'allpost':allpost, 'search':search}
    return render(request, 'home/search.html', params)

def write(request):
    if request.user.is_authenticated:
        messages.success(request, "You can Write your blog here")
        if request.method =='POST':
            title = request.POST['title']
            name = request.POST['name']
            categories = request.POST['categories']
            content = request.POST['content']
            slug = f"{name}-{categories}-{title}"
            # print(name, timestamp, categories, content, slug, title)
            if len(str(name))<2 or len(str(title))<5 or len(str(content))<10:
                messages.error(request, "Please fill the form Correctly")
            else:
                post = Post(title=title, name=name, Categories=categories, content=content, slug=slug)
                post.save()
                messages.success(request, "Post Added Successfully!")
    else:
        messages.error(request,"To write a post you have to Login First")
        return redirect('home')
    return render(request, 'home/write.html')

def feedback(request):
    messages.info(request, "Write your feedback")
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        x = datetime.datetime.now()
        timestamp = x.strftime("%c")
        if len(str(name))<2 or len(str(email))<7 or len(str(message))<5:
            messages.error(request, "Please fill the form Correctly")
        else:
            feedback = Feedback(name=name, email=email, message=message, timestamp=timestamp)
            feedback.save()
            send_mail(
            'Feedback from: ' + name,
            message,
            email,
            ['quaintvisionweb@gmail.com'],
            fail_silently=False,
            )
        messages.success(request, "Thanks for giving feedback")
    return render(request, "home/feedback.html")

def signup(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #Checking Wrong inputs

        # Username Must br under 20 Character
        if len(Username) > 20:
            messages.error(request, "Username must be under 20 Character")
            return redirect('home')
        
        #Select a unique username
        if not Username.isalnum():
            messages.error(request, "Username Should only contain letters and Number without Spacing (Do not use any special character)")
            return redirect('home')
        
        #Password should Match
        if pass1!=pass2:
            messages.error(request, "Passwords Do not match please fill the same password")
            return redirect('home')

        myuser = User.objects.create_user(Username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Account Created Successfully Please Click on the login Button and Get logged in.")
        return redirect('home')
    else:
        return HttpResponse("Not allowed")

def handellogin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        messages.warning(request, "Successfully Logged In")
        return redirect('home')
    else:
        messages.error(request, "Please fill the Correct Details")
        return redirect('home')
        
def handellogout(request):
    logout(request)
    messages.success(request, "Succesfully Logged out")
    return redirect('home')

def profile(request):
    return HttpResponse("edit")

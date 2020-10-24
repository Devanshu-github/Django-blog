from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here



def bloghome(request):
    allposts = Post.objects.all()[::-1]
    user = request.user
    context = {'allposts':allposts, 'user':user}
    return render(request, 'blog/bloghome.html', context)



def blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post)
    context = {"post":post, 'comments': comments, 'user': request.user}
    return render(request, 'blog/blogpost.html', context)

def blogComment(request):
    if request.method == "POST":
        comment =  request.POST.get('comment')
        user =  request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        comment = BlogComment(comment=comment, user=user, post=post)
        comment.save()
        messages.success(request, "Comment added successfully!!")
    return redirect(f"/blog/{post.slug}")
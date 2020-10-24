from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.contrib.auth import authenticate, login ,logout
# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    Categories = models.CharField(max_length=50)
    content = models.TextField()
    slug = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.title + " by " + self.name


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return self.comment[0:13] + " .... " + " By " + self.user.username
    
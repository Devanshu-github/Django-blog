from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=200)
    categories = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.CharField(max_length=30)

    def __str__(self):
        return ' Message From ' +  self.name  +  ' --> ' + self.email

class Feedback(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.CharField(max_length=30)

    def __str__(self):
        return 'Feedback from ' + self.name + ' --> ' + self.email 



from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='blog' , null=True)
    date_posted= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Contact(models.Model):
    Name = models.CharField(max_length = 100)
    Subject = models.CharField(max_length = 100)
    Email = models.EmailField()
    Message = models.TextField()

class Images(models.Model):
    Title = models.CharField(max_length=100)
    Image = models.ImageField(upload_to = 'media')
    Category = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    date_posted= models.DateTimeField(default=timezone.now)     

    def __str__(self):
        return self.Title

class Subscribe(models.Model):
    sys_id = models.AutoField(primary_key=True, null=False, blank=True)
    email = models.EmailField(null=False, blank=True, max_length=200, unique=True)
    status = models.CharField(max_length=64, null=False, blank=True)
    created_date = models.DateTimeField(null=False, blank=True)
    updated_date = models.DateTimeField(null=False, blank=True)

    def __str__(self):
        return self.email
   
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted= models.DateTimeField(default=timezone.now)
    authoer = models.ForeignKey(User, on_delete=models.CASCADE)

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

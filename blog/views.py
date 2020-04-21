import re
from django.shortcuts import render , get_object_or_404 ,redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib import messages
from .models import Post , Images , Subscribe
from .forms import ContactForm 
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def home(request):
   
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def projects(request):
    context = {
        'image': Images.objects.all()
    }
    return render(request, 'blog/project.html', context)

class ProjectListView(ListView):
    model = Images
    template_name = 'blog/Project.html'  #NOTE <app>/<model>_<viewtype>.html
    context_object_name = 'image'
    ordering = ['-date_posted']

# def contact(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)      
#         if form.is_valid():
#             subject = form.cleaned_data['Subject']
#             from_email= form.cleaned_data['Email']
#             message = form.cleaned_data['Message']
#             recipient_list = ['wildlifemain1@gmail.com']
#             try:
#                 send_mail(subject, message, from_email , recipient_list)
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             messages.success(request, "Thank you!")

#     form = ContactForm()

#     return render(request, 'blog/contact.html', {'title': 'Contact', 'form':form})


def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blog.html', context) #I must add title for the Blog! Remember that!

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'  #NOTE <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            email,
            ['mazenomar-@outlook.com']
        )
        messages.success(request, "Thank you for sending your email! I will answer you in less time")
    return render(request, 'blog/contact.html', {})


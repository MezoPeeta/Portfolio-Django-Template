from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post , Images
from .forms import ContactForm 


def home(request):
   
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def projects(request):
    context = {
        'image': Images.objects.all()
    }
    return render(request, 'blog/project.html', context, {'title': 'Projects'})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)      
        if form.is_valid():
            form.save()
    form = ContactForm()

    return render(request, 'blog/contact.html', {'title': 'Contact', 'form':form})

def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blog.html',context) #I must add title for the Blog! Remember that!





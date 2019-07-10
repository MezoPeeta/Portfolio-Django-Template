from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('projects/', views.projects, name='Projects'),
    path('contact/', views.contact, name='Contact'),
    path('blog/', views.blog, name='Blog'),


]
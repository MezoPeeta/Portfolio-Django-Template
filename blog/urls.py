from django.urls import path
from . import views
from .views import ProjectListView , PostListView

urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('portfolio/', ProjectListView.as_view(), name='Projects'),
    path('contact/', views.contact, name='Contact'),
    path('blog/',PostListView.as_view() , name='Blog'),

]
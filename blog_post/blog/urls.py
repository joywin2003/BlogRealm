from django.urls import path
from .views import PostListView, PostDetialView
from . import views

urlpatterns = [
    path('',PostListView.as_view() , name='blog-home'),
    path('post/<int:pk>/',PostDetialView.as_view() , name='post-detail'),
    path('about/', views.about, name='blog-about'),
]
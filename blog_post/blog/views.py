from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Post




def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blog/blog.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    ordering = '-date_posted'

class PostDetialView(DetailView):
    model = Post


def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})



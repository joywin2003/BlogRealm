from django.shortcuts import render
from django.http import HttpRequest, HttpResponse



posts = [
    {
        'author': 'Sam',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2020',
    },
    {
        'author': 'Joy',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2020',
    }
]


def home(request):
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})



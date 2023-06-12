from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('<h1>Blog page</h1>')
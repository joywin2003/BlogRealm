


<br>

## Installation:

1. Install Django: `pip install Django.     
2. Create a new Django project: `django-admin startproject project_name`.
3. Navigate to the project directory: `cd project_name`.
4. Create a Django app within the project: `python manage.py startapp app_name`.
5. Open the `views.py` file inside the app directory.
6. Create a view function in `views.py`.
7. Save the changes in `views.py`

```python
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def home(request): 
	return render(request, 'blog/blog.html')

def about(request):
	return HttpResponse(request, 'blog/about.html')
```
6. Open the `urls.py` file inside the app directory and define URL patterns
for example 
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]

```
7. Add the app's URL path to the project's `urls.py` file:
```python
from django.urls import include, path 

urlpatterns = [ 
	# other paths 
	path('blog/', include('blog.urls')), 
]
```
8. Run the development server: `python manage.py runserver`.
    
9. Open a web browser and visit [http://localhost:8000](http://localhost:8000/) to see your Django project running.
<br>
<br>

## Next Step

[Creating and Rending Templates](obsidian://open?vault=Django&file=Creating%20and%20Rendering%20Templates%20in%20Django)
<br>


1. Create a `static` folder in your Django app directory (if it doesn't exist already).
    
2. Inside the `static` folder, create subfolders named `css` and `js` to organize your CSS and JavaScript files, respectively.
    
3. In your HTML templates, you can refer to these static files using the `{% static %}` template tag.

Example:

```html
<!-- Include CSS -->
<link rel="stylesheet" type="text/css" href="{% static 'css/styles.css' %}">

<!-- Include JavaScript -->
<script src="{% static 'js/script.js' %}"></script>

```

In Django, there are no specific restrictions on the names of subfolders within the `static` directory. You can choose any meaningful names for your subfolders based on your project's organization and requirements.

# URL tag:

The `{% url %}` template tag in Django is used to dynamically generate URLs based on named routes or views. It helps avoid hardcoding URLs and makes templates more flexible

For example:
```html
<a class="nav-item nav-link" href="{% url 'blog-home' %}">Home</a>
<a class="nav-item nav-link" href="{% url 'blog-about' %}">About</a>
```
Here, the `{% url %}` tag generates the URLs for the `blog-home` and `blog-about` routes defined in `urls.py`.

```python
urlpatterns = [
	path('', views.home, name='blog-home'),
	path('about/', views.about, name='blog-about'),
]
```
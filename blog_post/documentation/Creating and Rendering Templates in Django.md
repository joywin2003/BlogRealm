<br>

## 1.  **Rendering Templates in Django**



1. Create a `templates` folder in your Django app.
    
2. Inside the `templates` folder, create a subfolder with the name of your app (e.g., "blog").

    
3. Place your HTML template files inside the app-specific folder.
    
4. In your project's `settings.py` file, locate the `INSTALLED_APPS` list.
    
5. Add your app to the `INSTALLED_APPS` list using the syntax `'app_name.apps.AppConfig'`. For example, if your app is named "blog", add `'blog.apps.BlogConfig'`.
    
6. Import the `render` function from Django's shortcuts module in your `views.py` file. Add the following line at the top of the file:
7. To render a template in Django, use the `render` function in your view function. For example, if you have a view function named `home`, and you want to render the `home.html` template located in the `blog` app, you would add the following code.
```python
from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')

```
8. Finally, run your Django project by executing the command `python manage.py runserver`

<br>
<br>

## 2. Passing an Argument to render

```python
def home(request):
	context = {'posts': posts}
	return render(request, 'blog/blog.html', context)
```
Here we are passing **context** to render 

<br>
<br>


## 3. Adding Django Templates

1. The notation `{% %}` is used in Django templates to mark the beginning and end of template tags. Django templates are used to dynamically generate HTML and other types of text-based content in web applications aka logic.
2. In Django templates, double curly braces `{{ }}` are used for template variables. They are used to output dynamic data from the view to the template.
	Example: {{ my_variable }}

For example :
```python
{% for post in posts %}
	<article>
		<h2>{{post.title}}</h2>
		<p>By {{post.author}} on {{post.date_posted}}</p>
		<p>{{post.content}}</p>
	</article>
{% endfor %}
```
 3. The `{% for %}` loop is used to iterate over a collection of items in Django templates. It allows you to repeat a block of code for each item in the collection. Within the loop, you can access the attributes of each item using `{{ }}` syntax to output their values in the template. The loop is closed with `{% endfor %}`.

4.   The `{% if %}` statement in Django templates  as shown
```python
{%if title%}
	<title>Django Blog - {{title}}</title>
{%else%}
	<title>Django Blog</title>
{%endif%}
```
<br>
<br>

## 4. Templete inheritance

Template inheritance in Django allows you to create a main template with common elements and structure. Child templates can then inherit this main template and add or modify specific content as needed. It helps in avoiding repetition and maintaining consistency throughout your website.

1. Create a base.html file in the templates folder.
2. Define common elements and structure in base.html.
3. Child templates start with `{% extends %}` and provide the path to base.html.
4. Use `{% block %}` in base.html to define overrideable sections.
5. Child templates use `{% block %}` to specify content to replace in base.html.
6. Add specific content and HTML markup in child templates as needed.

Example:

1. Consider blog.html as follows

```html
<!DOCTYPE html>
<html>
<head>
	{%if title%}
		<title>Django Blog - {{title}}</title>
	{%else%}
		<title>Django Blog</title>
	{%endif%}
</head>
<body>
{% for post in posts %}
	<h2>{{post.title}}</h2>
	<p>By {{post.author}} on {{post.date_posted}}</p>
	<p>{{post.content}}</p>
{% endfor %}
</body>
</html>
```


2. Let's consider a base.html file that defines the common elements and structure:

base.html:
```html
<!DOCTYPE html>
<html>
<head>
	{%if title%}
		<title>Django Blog - {{title}}</title>
	{%else%}
		<title>Django Blog</title>
	{%endif%}
</head>
<body>
{% block content %} {% endblock %}
</body>
</html>
```

3. In a child template, such as home.html, you can inherit from the base.html and provide specific content:

```html
{% extends "blog/base.html"%}
{% block content %}
{% for post in posts %}
	<h2>{{post.title}}</h2>
	<p>By {{post.author}} on {{post.date_posted}}</p>
	<p>{{post.content}}</p>
{% endfor %}
{% endblock content %}
```

The child template inherits the structure and common elements from the base.html and overrides the title and content blocks with specific content. This way, you can reuse the base.html and have consistent elements across multiple templates.

<br>

## Creating a superuser
1. Run the command `python manage.py migrate` to migrate
2. Run the following command to create a superuser:
```command
python manage.py createsuperuser
```
4. To access the Django admin interface, open a web browser and go to `http://localhost:8000/admin` (replace `localhost:8000` with your project's URL if necessary).
<br>
## Models

  
A model in Django is a Python class that represents a database table. It defines the structure and behaviour of the data stored in the database.

1. Open the `models.py` file inside the app directory.
2. Define a class that inherits from the `models.Model` class. This class represents a table in the database:
```python
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
```
3. Run the following command to create the necessary database tables based on your models:
```command
python manage.py makemigrations 
python manage.py migrate
```
5.  Your model is now ready to be used in your Django project. You can perform database operations on the model, such as creating, retrieving, updating, and deleting records.

<br>

## SQL migrations

<br> 

To generate the SQL migration code for your Django models, you can use the `sqlmigrate` management command in Django. Here's how you can do it:

```command
python manage.py sqlmigrate app_name migration_number
```
<br>

![[Screenshot 2023-06-15 at 8.43.40 PM.png]]
1. here app name is blog and migration number is 0001, 
<br>
2. Hence run the command for the above example as:
```command
python manage.py sqlmigrate blog 0001

```

![[Screenshot 2023-06-15 at 8.44.45 PM.png]]
3.  you can also check it in migrations files
4. then migrate the change by 'python manage.py migrate'

## Search

1. by username
```command
User.objects.filter(username="Joywin").first()
```

2. By UserID
```command
User.objects.get(id=1)
```

3. Check for posts(in blog project)
```command
Post.objects.all()
```

These are the commands I used but there are variety of functions associated with the object class explore in Django official docs or for Pros Chatgpt

### How to add Post and save post

![[Screenshot 2023-06-15 at 10.57.32 PM.png]]
Save the data in the database by adding post_!.save()
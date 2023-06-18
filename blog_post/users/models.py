from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.png", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"
    
    def save(self):
        super().save()

        if self.image.height >300 or self.image.width >300:
            output_size = (300,300)
            img = Image.open(self.image.path)
            img.thumbnail(output_size)
            img.save(self.image.path)



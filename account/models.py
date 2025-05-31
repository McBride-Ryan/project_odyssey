# accounts/models.py
from django.db import models
from django.contrib.auth.models import User
from PIL import Image # Make sure Pillow is installed: pip install Pillow


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # CHANGE THIS LINE
    def save(self, *args, **kwargs): # <--- ADD *args, **kwargs here
        super().save(*args, **kwargs) # <--- And pass them here

        # Your image resizing logic (which is fine where it is, after super().save())
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
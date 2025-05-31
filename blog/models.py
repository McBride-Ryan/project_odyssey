from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    source = models.CharField(null=True, blank=True)
    description	= models.CharField(null=True, blank=True)
    published_at = models.DateTimeField(default=timezone.now)
    story = HTMLField(null=True, blank=True)
    type = models.CharField(null=True, blank=True)
    hero = models.CharField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
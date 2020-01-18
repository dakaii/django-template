from django.db import models


class Post(models.Model):
    caption = models.TextField()
    # picture = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

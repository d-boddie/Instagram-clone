from django.db import models
from django.utils import timezone

# Create your models here.


class Comment(models.Model):
    post = models.TextField(max_length=280)
    created_at = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)


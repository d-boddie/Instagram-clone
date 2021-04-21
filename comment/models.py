from django.db import models
from django.utils import timezone
from photo.models import Photo
from authentication.models import InstagramUser

# Create your models here.


class Comment(models.Model):
    creator = models.ForeignKey(
        InstagramUser, related_name="creator", on_delete=models.CASCADE, default=True)
    post = models.TextField(max_length=280)
    created_at = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    photo = models.ForeignKey(
        Photo, related_name="photo", on_delete=models.CASCADE, default=True)
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return self.creator
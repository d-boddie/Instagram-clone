from django.db import models
from django.utils import timezone
from authentication.models import InstagramUser
from comment.models import Comment


# Create your models here.
class Photo(models.Model):
    caption = models.CharField(max_length=280, null=True, blank=True)
    image = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(InstagramUser)
    total_likes = models.IntegerField(default=0)
    button = models.CharField(max_length=50, default="Like")
    poster = models.ForeignKey(
        InstagramUser, related_name="poster", on_delete=models.CASCADE, default=True)

    comment = models.ForeignKey(
        Comment, related_name="comment", on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.caption
    
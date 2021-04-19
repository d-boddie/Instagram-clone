from django.db import models
from django.utils import timezone
from authentication.models import InstagramUser

class Message(models.Model):
    creator = models.ForeignKey(InstagramUser, related_name='message',
                                on_delete=models.CASCADE)
    message = models.CharField(max_length=280)
    created_at = models.DateTimeField(default=timezone.now)
    to = models.ForeignKey(InstagramUser, related_name='to',
                                on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    total = models.IntegerField(default=0)
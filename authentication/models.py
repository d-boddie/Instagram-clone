from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class InstagramUser(AbstractUser):
    bio = models.TextField(max_length= 100, blank=True)
    website = models.URLField(max_length=100, blank=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=30)
    display_name = models.CharField(max_length=20)
    follow = models.ManyToManyField('self', related_name="follows", symmetrical=False, 
            blank=True)

    def count_followers(self):
        return self.follow.count()

    def __str__(self):
        return self.username
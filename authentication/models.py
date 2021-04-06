from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class InstagramUser(AbstractUser):
    # username = models.CharField(max_length=20, null=True, blank=True)
    # password = models.CharField(max_length=10)
    # email = models.EmailField(max_length=50, null=False, blank=False)
    bio = models.TextField(max_length= 100, blank=True)
    website = models.URLField(max_length=100, blank=True)
    display_name = models.CharField(max_length=20)


    def __str__(self):
        return self.username
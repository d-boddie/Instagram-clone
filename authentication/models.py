from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class InstagramUser(AbstractUser):
    bio = models.TextField(max_length= 100, blank=True)
    website = models.URLField(max_length=100, blank=True)
    display_name = models.CharField(max_length=20)
    friends = models.ManyToManyField('self', related_name="friend", symmetrical=False, 
            blank=True)
<<<<<<< HEAD
    avatar = models.ImageField(upload_to='photos/', blank=True, null=True)
=======
    follower = models.IntegerField(default=0)
>>>>>>> 54bfee2514b53c91f01698951479b369b86cdfdc

    def count_friends(self):
        return self.friend.count()

    def count_follower(self):
        return self.follower.count()
        
    def __str__(self):
        return self.username
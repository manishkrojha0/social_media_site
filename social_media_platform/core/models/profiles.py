from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    """Model class Profile."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, null=True, blank=True)
    followers = models.ManyToManyField(User, related_name='followers')
    followings = models.ManyToManyField(User, related_name='following')

    def __str__(self) -> str:
        return self.user.username
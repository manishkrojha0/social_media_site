from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Model class for post"""
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self) -> str:
        return f"Post {self.id}: {self.title}"

    

from django.db import models
from django.contrib.auth.models import User
from core.models.post import Post

class Comment(models.Model):
    """Model class for comment."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey("Profile", on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=True)


    def __str__(self) -> str:
        return self.description
    
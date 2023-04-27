from django.db import models
from django.contrib.auth.models import User

class Like(models.Model):
    """Model class for like."""
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name='likes')
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE, related_name='likes', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

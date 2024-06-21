from datetime import datetime
from django.db import models

class Comment(models.Model):
    username = models.CharField(max_length=10, null=False)
    email = models.EmailField(max_length=20, unique=True, null=False)
    text = models.CharField(max_length=500)
    created = models.DateTimeField(default=datetime.now)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text[:20]}"
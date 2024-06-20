from django.db import models

class User(models.Model):
    username = models.CharField(max_length=10, null=False)
    email = models.EmailField(max_length=20, unique=True, null=False)

    def __str__(self):
        return f"{self.username}"

class Comment(models.Model):
    user = User()
    text = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text}"
from django.contrib.auth.models import AbstractUser
from django.db import models

def avatar_upload_path(instance, filename):
    return f'avatars/user_{instance.id}/{filename}'

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to=avatar_upload_path, default='avatars/default.png')
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    notify_on_follow  = models.BooleanField(default=True)
    notify_on_like    = models.BooleanField(default=True)
    notify_on_comment = models.BooleanField(default=True)

    def __str__(self):
        return self.username

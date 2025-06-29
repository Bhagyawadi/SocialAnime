from django.db import models
from django.conf import settings

class Notification(models.Model):
    NOTIF_TYPES = [('follow','Follow'),('like','Like'),('comment','Comment')]
    to_user     = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notifications', on_delete=models.CASCADE)
    from_user   = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    notif_type  = models.CharField(max_length=10, choices=NOTIF_TYPES)
    post        = models.ForeignKey('posts.Post', null=True, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    read        = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

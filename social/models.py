from django.db import models
from django.conf import settings

class Follow(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 related_name='following_set',
                                 on_delete=models.CASCADE)
    following = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  related_name='followers_set',
                                  on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f"{self.follower} → {self.following}"

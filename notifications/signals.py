from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from social.models import Follow
from posts.models import Comment, Post
from notifications.models import Notification

@receiver(post_save, sender=Follow)
def follow_notif(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            to_user=instance.following,
            from_user=instance.follower,
            notif_type='follow'
        )

@receiver(m2m_changed, sender=Post.likes.through)
def like_notif(sender, instance, action, pk_set, **kwargs):
    if action == 'post_add':
        for user_id in pk_set:
            Notification.objects.create(
                to_user=instance.author,
                from_user_id=user_id,
                notif_type='like',
                post=instance
            )

@receiver(post_save, sender=Comment)
def comment_notif(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            to_user=instance.post.author,
            from_user=instance.author,
            notif_type='comment',
            post=instance.post
        )

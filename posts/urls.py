from django.urls import path
from posts import views as post_views
from social import views as social_views

urlpatterns = [
    # Feed
    path('', social_views.feed_view, name='feed'),

    # Posts
    path('create/', post_views.create_post_view, name='create_post'),
    path('post/<int:post_id>/edit/', post_views.edit_post, name='edit_post'),
    path('post/<int:post_id>/delete/', post_views.delete_post, name='delete_post'),

    # Likes & Comments
    path('like/', post_views.toggle_like, name='toggle_like'),
    path('comment/<int:post_id>/', post_views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/delete/', post_views.delete_comment, name='delete_comment'),
]

from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from posts.models import Post
from .models import Follow
from posts.forms import CommentForm
from accounts.models import CustomUser
from django.core.paginator import Paginator

@login_required
def toggle_follow(request, username):
    target = get_object_or_404(CustomUser, username=username)
    if request.user == target:
        return redirect('profile', username=username)

    rel, created = Follow.objects.get_or_create(
        follower=request.user,
        following=target
    )
    if not created:
        rel.delete()

    return redirect('profile', username=username)

@login_required
def feed_view(request):
    # IDs of users you follow, plus yourself
    following_ids = list(
        request.user.following_set.values_list('following_id', flat=True)
    ) + [request.user.id]
    post_list = Post.objects.filter(author__in=following_ids).order_by('-created_at')

    paginator = Paginator(post_list, 5)  # 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'posts/feed.html', {
        'page_obj': page_obj,
        'comment_form': CommentForm(),
    })
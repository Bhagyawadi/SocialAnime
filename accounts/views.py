from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from social.models import Follow
from .models import CustomUser

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('feed')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile_view(request, username):
    # Load the profile user using the CustomUser class
    user_profile = get_object_or_404(CustomUser, username=username)

    # Determine follow status (only if not your own profile)
    is_following = False
    if request.user != user_profile:
        is_following = Follow.objects.filter(
            follower=request.user,
            following=user_profile
        ).exists()

    # Counts
    followers_count = Follow.objects.filter(following=user_profile).count()
    following_count = Follow.objects.filter(follower=user_profile).count()

    return render(request, 'accounts/profile.html', {
        'user_profile': user_profile,
        'is_following': is_following,
        'followers_count': followers_count,
        'following_count': following_count,
    })
    
@login_required
def edit_profile_view(request, username):
    if request.user.username != username:
        return redirect('profile', username=request.user.username)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'accounts/edit_profile.html', {'form': form})

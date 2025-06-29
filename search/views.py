from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from posts.models import Post
from .forms import SearchForm
from django.db.models import Q
from django.core.paginator import Paginator

@login_required
def search_view(request):
    form = SearchForm(request.GET or None)
    users = []
    post_list = []

    if form.is_valid():
        q = form.cleaned_data['q']
        users = CustomUser.objects.filter(
            Q(username__icontains=q) | Q(bio__icontains=q)
        )
        post_list = Post.objects.filter(caption__icontains=q).order_by('-created_at')

    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page')
    post_page = paginator.get_page(page_number)

    return render(request, 'search/results.html', {
        'form': form, 'users': users, 'post_page': post_page, 'query': request.GET.get('q','')
    })

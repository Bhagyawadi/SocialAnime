from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def notif_list(request):
    # 1) Fetch unread notifications into a Python list
    unread_qs = request.user.notifications.filter(read=False)
    notifs = list(unread_qs)

    # 2) Mark them read in the DB
    unread_qs.update(read=True)

    # 3) Render, passing the list
    return render(request, 'notifications/list.html', {'notifications': notifs})

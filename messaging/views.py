from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Conversation, Message
from .forms import MessageForm
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def conv_list(request):
    """
    List all conversations for the current user.
    """
    convos = Conversation.objects.filter(participants=request.user)
    return render(request, 'messaging/conversations.html', {'convos': convos})

@login_required
def conv_detail(request, conv_id=None, other_username=None):
    # If starting a new conversation by username
    if other_username:
        other = get_object_or_404(User, username=other_username)
        # Look for an existing conversation between the two
        convos = Conversation.objects.filter(participants=request.user) \
                                      .filter(participants=other)
        if convos.exists():
            conv = convos.first()
        else:
            conv = Conversation.objects.create()
            conv.participants.add(request.user, other)

    # Otherwise, viewing by conv_id
    else:
        conv = get_object_or_404(Conversation, id=conv_id, participants=request.user)

    # Handle message form
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.conversation = conv
            msg.sender = request.user
            msg.save()
            return redirect('conv_detail', conv_id=conv.id)
    else:
        form = MessageForm()

    return render(request, 'messaging/detail.html', {
        'conversation': conv,
        'form': form,
    })
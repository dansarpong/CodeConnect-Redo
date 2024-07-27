from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError

from .models import Chatroom


@login_required
def create_chatroom(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        auth_link = generate_unique_auth_link()
        chatroom = Chatroom(name=name, description=description, created_by=request.user, auth_link=auth_link)
        
        try:
            chatroom.clean()
            chatroom.save()
            chatroom.add_member(request.user)
            chatroom.add_admin(request.user)
            return redirect('chatroom', chatroom_id=chatroom.id)
        except ValidationError as e:
            return render(request, 'core/create_channel.html', {'error': e.message})

    return render(request, 'core/create_channel.html')

@login_required
def join_chatroom(request):
    if request.method == "POST":
        auth_link = request.POST.get('auth_link')

        try:
            chatroom = Chatroom.objects.get(auth_link=auth_link)
            chatroom.add_member(request.user)
            return redirect('chatroom', chatroom_id=chatroom.id)
        except Chatroom.DoesNotExist:
            return render(request, 'core/join_channel.html', {'error': 'Invalid authentication link.'})

    return render(request, 'core/join_channel.html')

@login_required
def leave_chatroom(request, chatroom_id):
    chatroom = get_object_or_404(Chatroom, id=chatroom_id)
    chatroom.remove_member(request.user)
    return redirect('dashboard')

@login_required
def chatroom(request, chatroom_id):
    chatroom = get_object_or_404(Chatroom, id=chatroom_id)
    if request.user not in chatroom.members.all():
        return redirect('set_error', message="You are not a member of this chatroom.")
    rooms_joined = Chatroom.objects.filter(members=request.user)
    print(rooms_joined)
    return render(request, 'core/channel.html', {'chatroom': chatroom, 'rooms_joined': rooms_joined})

def generate_unique_auth_link():
    import uuid
    while True:
        auth_link = str(uuid.uuid4())
        if not Chatroom.objects.filter(auth_link=auth_link).exists():
            return auth_link

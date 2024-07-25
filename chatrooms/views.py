from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Chatroom


@login_required
def create_chatroom(request):
    if request.method == "POST":
        name = request.POST.get('name')
        auth_link = generate_unique_auth_link()
        chatroom = Chatroom.objects.create(name=name, created_by=request.user, auth_link=auth_link)
        chatroom.add_member(request.user)
        chatroom.add_admin(request.user)
        return redirect('chatroom', chatroom_id=chatroom.id)
    return render(request, 'core/create_chatroom.html')

@login_required
def join_chatroom(request, auth_link):
    chatroom = get_object_or_404(Chatroom, auth_link=auth_link)
    chatroom.add_member(request.user)
    return redirect('chatroom', chatroom_id=chatroom.id)

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
    return render(request, 'core/chatroom.html', {'chatroom': chatroom})

def generate_unique_auth_link():
    import uuid
    return str(uuid.uuid4())

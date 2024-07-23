from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomPasswordResetForm, CustomSetPasswordForm
from .models import Chatroom
from django.views.generic.edit import FormView


@login_required
def create_chatroom(request):
    if request.method == "POST":
        name = request.POST.get('name')
        auth_link = generate_unique_auth_link()
        chatroom = Chatroom.objects.create(name=name, created_by=request.user, auth_link=auth_link)
        chatroom.add_member(request.user)
        chatroom.add_admin(request.user)
        return redirect('dashboard')
    return render(request, 'core/create_chatroom.html')

@login_required
def join_chatroom(request, auth_link):
    chatroom = get_object_or_404(Chatroom, auth_link=auth_link)
    chatroom.add_member(request.user)
    return redirect('dashboard')

def generate_unique_auth_link():
    import uuid
    return str(uuid.uuid4())


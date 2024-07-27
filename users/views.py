from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from chatrooms.models import Chatroom
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomPasswordResetForm, CustomSetPasswordForm


def signin(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'core/signin.html', {'error_occured': True})
    else:
        return render(request, 'core/signin.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/signup.html', {'form': form})

def error_page(request):
    message = request.session.get('error_message', 'An error occurred.')
    return render(request, 'core/error_page.html', {'message': message})

def set_error(request, message):
    request.session['error_message'] = message
    return redirect('error_page')

@login_required
def profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'core/profile.html', {'form': form})

@login_required
def dashboard(request):
    rooms_joined = Chatroom.objects.filter(members=request.user)
    print(rooms_joined)
    if not rooms_joined.exists():
        return render(request, 'core/fresh_view.html')
    return render(request, 'core/dashboard.html', {'rooms_joined': rooms_joined})

@login_required
@xframe_options_exempt
def basic_view(request):
    return render(request, 'core/basic_view.html')

@login_required
@xframe_options_exempt
def fresh_view(request):
    return render(request, 'core/fresh_view.html')

class CustomPasswordResetView(PasswordResetView):
    template_name = 'core/password_reset.html'
    email_template_name = 'core/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'core/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'core/password_reset_confirm.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'core/password_reset_complete.html'

from django.contrib import admin
from django.urls import path, include
import users.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', users.views.login_user, name='login'),
    path('register/', users.views.register, name='register'),
    path('dashboard/', users.views.dashboard, name='dashboard'),
    path('profile/', users.views.profile, name='profile'),
    path('password_reset/', users.views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', users.views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', users.views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', users.views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('accounts/', include('django.contrib.auth.urls')),
]

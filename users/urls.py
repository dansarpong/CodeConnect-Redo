from django.urls import path
from . import views


urlpatterns = [
    path('', users.views.dashboard, name='dashboard'),
    path('signin/', users.views.signin, name='signin'),
    path('signup/', users.views.signup, name='signup'),
    path('profile/', users.views.profile, name='profile'),
    path('error_page/', users.views.error_page, name='error_page'),
    path('basic_view/', users.views.basic_view, name='basic_view'),
    path('fresh_view/', users.views.fresh_view, name='fresh_view'),
    path('set_error/<str:message>/', users.views.set_error, name='set_error'),

    path('password_reset/', users.views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', users.views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', users.views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', users.views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('error_page/', views.error_page, name='error_page'),
    path('basic_view/', views.basic_view, name='basic_view'),
    path('fresh_view/', views.fresh_view, name='fresh_view'),
    path('set_error/<str:message>/', views.set_error, name='set_error'),

    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

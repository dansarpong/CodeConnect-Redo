from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('fresh_view/', views.fresh_view, name='fresh_view'),
    path('error_page/', views.error_page, name='error_page'),
    path('set_error/<str:message>/', views.set_error, name='set_error'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
]

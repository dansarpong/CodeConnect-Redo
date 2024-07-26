from django.urls import path
from . import views


urlpatterns = [
    path('chatroom/<int:chatroom_id>/', views.chatroom, name='chatroom'),
    path('create/', views.create_chatroom, name='create_chatroom'),
    path('join/', views.join_chatroom, name='join_chatroom'),
    path('leave/<int:chatroom_id>/', views.leave_chatroom, name='leave_chatroom'),
]

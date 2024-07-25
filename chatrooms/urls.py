from django.urls import path
from . import views


urlpatterns = [
    path('chatroom/<int:chatroom_id>/', chatrooms.views.chatroom, name='chatroom'),
    path('create_chatroom/', chatrooms.views.create_chatroom, name='create_chatroom'),
    path('join_chatroom/', chatrooms.views.join_chatroom, name='join_chatroom'),
    path('leave_chatroom/<int:chatroom_id>/', chatrooms.views.leave_chatroom, name='leave_chatroom'),
]

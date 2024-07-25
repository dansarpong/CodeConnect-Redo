from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/chatrooms/<int:chatroom_id>/', consumers.ChatConsumer.as_asgi()),
]

from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/chatrooms/<str:room_name>/', consumers.ChatroomConsumer.as_asgi()),
]

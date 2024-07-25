import json
from datetime import datetime
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model

from .models import Chatroom, Message


User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chatroom_id = self.scope['url_route']['kwargs']['chatroom_id']
        self.chatroom_group_name = f'chat_{self.chatroom_id}'

        await self.channel_layer.group_add(
            self.chatroom_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.chatroom_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        user = self.scope['user']

        chatroom = await self.get_chatroom(self.chatroom_id)
        await self.save_message(user, chatroom, message)

        timestamp = await self.get_last_message_timestamp()

        await self.channel_layer.group_send(
            self.chatroom_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': user.username,
                'timestamp': timestamp,
                'sender_channel_name': self.channel_name,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        user = event['user']
        timestamp = event['timestamp']
        sender_channel_name = event['sender_channel_name']

        if self.channel_name != sender_channel_name:
            await self.send(text_data=json.dumps({
                'message': message,
                'user': user,
                'timestamp': timestamp,
            }))

    @database_sync_to_async
    def get_chatroom(self, chatroom_id):
        return Chatroom.objects.get(pk=chatroom_id)

    @database_sync_to_async
    def save_message(self, user, chatroom, message):
        return Message.objects.create(user=user, chatroom=chatroom, content=message)

    @database_sync_to_async
    def get_last_message_timestamp(self):
        last_message = Message.objects.last()
        return last_message.timestamp.strftime('%H:%M')
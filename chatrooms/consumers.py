import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Chatroom, Message
from django.contrib.auth import get_user_model

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

        await self.channel_layer.group_send(
            self.chatroom_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': user.username,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        user = event['user']

        await self.send(text_data=json.dumps({
            'message': message,
            'user': user,
        }))

    @database_sync_to_async
    def get_chatroom(self, chatroom_id):
        return Chatroom.objects.get(pk=chatroom_id)

    @database_sync_to_async
    def save_message(self, user, chatroom, message):
        return Message.objects.create(user=user, chatroom=chatroom, content=message)

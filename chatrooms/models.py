from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


CustomUser = get_user_model()

class Chatroom(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='chatrooms')
    members = models.ManyToManyField(CustomUser, related_name='joined_chatrooms', blank=False)
    admins = models.ManyToManyField(CustomUser, related_name='admin_chatrooms', blank=True)
    auth_link = models.CharField(max_length=255, unique=True)

    def add_member(self, user):
        self.members.add(user)

    def remove_member(self, user):
        self.members.remove(user)

    def add_admin(self, user):
        self.admins.add(user)

    def remove_admin(self, user):
        self.admins.remove(user)

    def clean(self):
        if not self.name:
            raise ValidationError("Name is required.")

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
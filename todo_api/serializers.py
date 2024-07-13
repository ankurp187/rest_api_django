from rest_framework import serializers

from djoser.serializers import UserSerializer, UserCreateSerializer as BaseUserSerializer

from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["task","completed","timestamp","updated","user"]


class UserCreateSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id','email','username','password']


class CurrentUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ['id','email','username','password']



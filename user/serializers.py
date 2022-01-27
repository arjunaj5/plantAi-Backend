from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'role']


class UserAuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'password']
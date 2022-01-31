from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .models import Plants


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(
                queryset=User.objects.all(),
                message="This email is already in use."
            )]
            )
    username = serializers.CharField(
            max_length=32,
            validators=[UniqueValidator(
                queryset=User.objects.all(),
                message="This username is already in use."
            )]
            )
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class PlantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plants
        fields = '__all__'

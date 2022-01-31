
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Plants

from rest_framework import status
from .serializers import UserSerializer, PlantsSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class UserCreate(APIView):
    """
    Creates the user.
    """
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlantsView(APIView):
    def get(self, request):
        plants = Plants.objects.all()
        serializer = PlantsSerializer(plants, many=True)
        return Response(serializer.data)

    def post(self, request, format='json'):
        serializer = PlantsSerializer(data=request.data)
        if serializer.is_valid():
            plant = serializer.save()
            if plant:
                print(plant)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


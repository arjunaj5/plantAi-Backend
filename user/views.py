from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer, UserAuthenticationSerializer


@api_view(['GET'])
def get_user(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def verify_user(request):
    print(request.data)
    serializer = UserAuthenticationSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.data['name']
        password = serializer.data['password']

        response = {"validated": False, "userExists": False}
        if not User.objects.filter(name=name):
            return Response(response)

        auth = User.objects.filter(name=name, password=password)
        if auth:
            return Response({"validated": True})
        else:
            response["userExists"] = True
            return Response(response)
    else:
        return Response("invalid data")

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import Plants
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
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

        # Get a list of plants based on search query
        print(request.data)
        if request.data['searchQuery']:
            queryset = Plants.objects.filter(name__icontains=request.data['searchQuery'])
            serializer = PlantsSerializer(queryset, many=True)
            return Response(serializer.data)

        # Insert a plant in database
        else:
            serializer = PlantsSerializer(data=request.data)
            if serializer.is_valid():
                plant = serializer.save()
                if plant:
                    print(plant)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        return Response({'token': token.key, 'user': UserSerializer(user).data})


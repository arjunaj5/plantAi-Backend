from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
import base64
from django.core.files.base import ContentFile
from .ml import detect_disease

from .serializers import UploadsSerializer, DiseasesSerializer

from .models import Diseases


class ExampleView(APIView):
    """
    A view that can accept POST requests with JSON content.
    """
    parser_classes = [FormParser, MultiPartParser]

    def post(self, request):
        data = request.data['photo']
        print(data)
        # format, imgstr = data.split(';base64,', -1)
        # ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(data), name='temp.jpg')

        serializer = UploadsSerializer(data={'photo': data})
        if serializer.is_valid():
            print("success")
            disease_image = serializer.save()
            path = "media/" + str(disease_image.photo)
            print(path)
            ml_id = detect_disease(path)
            if ml_id in [1, 4, 14]:
                return Response({"healthy": True})
            result = Diseases.objects.get(ml_id=ml_id)
            serializer = DiseasesSerializer(result)
            return Response(serializer.data)
        return Response({"result": "image not valid"})

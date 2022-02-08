from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
import base64
from django.core.files.base import ContentFile
from .ml import detect_disease
from .imagekit_upload import upload_to_imagekit

from .serializers import UploadsSerializer, DiseasesSerializer, DetectionHistorySerializer

from .models import Diseases


class DiseaseDetectionView(APIView):
    """
    A view that can accept POST requests with JSON content.
    """
    parser_classes = [FormParser, MultiPartParser]

    def post(self, request):
        data64 = request.data['photo']
        # format, imgstr = data64.split(';base64,')
        # ext = format.split('/')[-1]
        # data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        data = ContentFile(base64.b64decode(data64), name='temp.jpg')

        serializer = UploadsSerializer(data={'photo': data})
        if serializer.is_valid():
            print("success")
            disease_image = serializer.save()
            path = "media/" + str(disease_image.photo)
            print(path)
            ml_id = detect_disease(path)
            if ml_id in [1, 4, 14]:
                return Response({"healthy": True})
            disease_data = Diseases.objects.get(ml_id=ml_id)
            serializer = DiseasesSerializer(disease_data)
            return Response(serializer.data)
        return Response({"result": "image not valid"})


class DiseaseImageUploadToImagekitView(APIView):
    def post(self, request):
        user_id = request.data['userId']
        disease_data = Diseases.objects.get(ml_id=request.data['mlId'])
        url = upload_to_imagekit(request.data['base64'])
        detection_history_data = {"leaf_url": url, "disease": disease_data.id, 'user': user_id}
        detection_history_serializer = DetectionHistorySerializer(data=detection_history_data)
        if detection_history_serializer.is_valid():
            detection_history_serializer.save()
            return Response(detection_history_serializer.data, status=status.HTTP_201_CREATED)
        return Response(detection_history_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

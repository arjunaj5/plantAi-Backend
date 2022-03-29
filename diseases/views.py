from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
import base64
from django.core.files.base import ContentFile
from .ml import detect_disease
from .imagekit_upload import upload_to_imagekit

from .serializers import UploadsSerializer, DiseasesSerializer, DetectionHistorySerializer, DetailsFromDiseaseIdSerializer

from .models import Diseases, DetectionHistory


class DiseaseDetectionView(APIView):
    """
    A view that can accept POST requests with JSON content.
    """
    parser_classes = [FormParser, MultiPartParser]

    def post(self, request):
        data64 = request.data['photo']
        data = ContentFile(base64.b64decode(data64), name='temp.jpg')

        serializer = UploadsSerializer(data={'photo': data})
        if serializer.is_valid():
            print("success")
            disease_image = serializer.save()
            path = "media/" + str(disease_image.photo)
            print(path)
            ml_result = detect_disease(path)
            ml_id = ml_result["id"]
            probability = ml_result["probability"]
            if ml_id in [3, 4, 6, 10, 14, 17, 19, 22, 23, 24, 27, 37]:
                return Response({"healthy": True, "probability": probability})
            disease_data = Diseases.objects.get(ml_id=ml_id)
            serializer = DiseasesSerializer(disease_data)
            serializer_data = serializer.data
            serializer_data.update({"probability": probability})
            return Response(serializer_data)
        return Response({"result": "image not valid"})


class DiseaseImageUploadToImagekitView(APIView):
    def post(self, request):
        user_id = request.data['userId']
        url = upload_to_imagekit(request.data['base64'])
        probability = request.data['probability']
        detection_history_data = {'probability': probability}

        # for healthy detection, we store disease_id as null value in detection History table
        healthy = request.data['healthy']
        if healthy == 'true':
            detection_history_data.update({"leaf_url": url, 'user': user_id, 'detected': False})
        if healthy == 'false':
            # for detected disease, mlId will be send by client
            disease_data = Diseases.objects.get(ml_id=request.data['mlId'])
            detection_history_data.update({"leaf_url": url, "disease": disease_data.id, 'user': user_id})
        detection_history_serializer = DetectionHistorySerializer(data=detection_history_data)
        if detection_history_serializer.is_valid():
            detection_history_serializer.save()
            return Response(detection_history_serializer.data, status=status.HTTP_201_CREATED)
        return Response(detection_history_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserHistory(APIView):
    def post(self, request):
        queryset = DetectionHistory.objects.filter(user=request.data['id']).filter(detected=True).order_by('-id')
        serializer = DetectionHistorySerializer(queryset, many=True)
        return Response(serializer.data)


class DetailsFromDiseaseId(APIView):
    def post(self, request):
        queryset = Diseases.objects.get(pk=request.data['disease_id'])
        serializer = DetailsFromDiseaseIdSerializer(queryset)
        return Response(serializer.data)

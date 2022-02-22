from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import ReportsSerializer, AdminReportsSerializer, NewDiseaseSerializer, NewCureSerializer
from .models import Reports
from diseases.models import DetectionHistory


class ReportsCreationView(APIView):

    def post(self, request):

        serializer = ReportsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            history = DetectionHistory.objects.get(pk=request.data['history'])
            history.reported = True
            history.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ReportsRetrievalView(APIView):
    def post(self, request):
        queryset = Reports.objects.filter(history__user=request.data['user_id']).order_by('-id')
        serializer = ReportsSerializer(queryset, many=True)
        return Response(serializer.data)


class AllReportsRetrievalView(APIView):
    def get(self, request):
        queryset = Reports.objects.all().order_by('-id')
        serializer = AdminReportsSerializer(queryset, many=True)
        return Response(serializer.data)


class NewDiseaseView(APIView):

    def post(self, request):
        serializer = NewDiseaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            report = Reports.objects.get(pk=request.data['report'])
            report.status = 'replied'
            report.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class NewCureView(APIView):

    def post(self, request):
        serializer = NewCureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            report = Reports.objects.get(pk=request.data['report'])
            report.status = 'replied'
            report.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
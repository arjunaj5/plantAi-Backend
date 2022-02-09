from rest_framework import serializers
from .models import Uploads, Diseases, DetectionHistory


class UploadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uploads
        fields = '__all__'


class DiseasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diseases
        fields = '__all__'


class DetailsFromDiseaseIdSerializer(serializers.ModelSerializer):
    plant_name = serializers.ReadOnlyField(source='plant.name')

    class Meta:
        model = Diseases
        fields = ['plant_name']


class DetectionHistorySerializer(serializers.ModelSerializer):
    disease_name = serializers.ReadOnlyField(source='disease.name', allow_null=True)

    class Meta:
        model = DetectionHistory
        fields = '__all__'

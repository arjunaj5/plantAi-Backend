from rest_framework import serializers
from .models import Reports


class ReportsSerializer(serializers.ModelSerializer):
    detected = serializers.ReadOnlyField(source='history.detected')
    disease = serializers.ReadOnlyField(source='history.disease.name')

    class Meta:
        model = Reports
        fields = '__all__'


class AdminReportsSerializer(serializers.ModelSerializer):
    detected = serializers.ReadOnlyField(source='history.detected')
    disease = serializers.ReadOnlyField(source='history.disease.name')
    plant = serializers.ReadOnlyField(source='history.disease.plant.name')
    disease_url = serializers.ReadOnlyField(source='history.leaf_url')

    class Meta:
        model = Reports
        fields = '__all__'

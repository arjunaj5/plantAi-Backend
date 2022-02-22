from rest_framework import serializers
from .models import Reports, NewDisease, NewCure


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


class NewDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewDisease
        fields = '__all__'


class NewCureSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewCure
        fields = '__all__'

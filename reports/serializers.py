from rest_framework import serializers
from .models import Reports


class ReportsSerializer(serializers.ModelSerializer):
    detected = serializers.ReadOnlyField(source='history.detected')
    disease = serializers.ReadOnlyField(source='history.disease.name')

    class Meta:
        model = Reports
        fields = '__all__'

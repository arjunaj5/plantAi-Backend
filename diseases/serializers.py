from rest_framework import serializers
from .models import Uploads, Diseases


class UploadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uploads
        fields = '__all__'

class DiseasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diseases
        fields = '__all__'

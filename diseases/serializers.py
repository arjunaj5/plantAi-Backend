from rest_framework import serializers
from .models import Uploads


class UploadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uploads
        fields = '__all__'

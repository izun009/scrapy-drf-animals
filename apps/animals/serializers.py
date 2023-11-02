# api/serializers.py

from rest_framework import serializers
from .models import Animals

class AnimalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animals
        fields = ('name', 'fact', 'description', 'image_urls')

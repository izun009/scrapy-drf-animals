# api/serializers.py

from rest_framework import serializers
from .models import Animals

# class AnimalsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Animals
#         fields = ('name', 'fact', 'description', 'image_urls')

class FactsSerializer(serializers.Serializer):
    fact = serializers.CharField()
    description = serializers.CharField()

class AnimalsSerializer(serializers.ModelSerializer):
    facts = FactsSerializer(many=True)

    class Meta:
        model = Animals
        fields = ('name', 'facts', 'image_urls')

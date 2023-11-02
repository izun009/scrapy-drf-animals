from django.shortcuts import render
from rest_framework import generics, permissions, status

# Create your views here.
from .models import Animals
from rest_framework import viewsets, permissions
from .serializers import AnimalsSerializer


class AnimalsViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Animals.objects.all()
    serializer_class = AnimalsSerializer
    permission_classes = [permissions.IsAuthenticated]


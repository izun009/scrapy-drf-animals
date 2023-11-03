# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Animals
from .serializers import AnimalsSerializer

class AnimalsListView(APIView):
    def get(self, request):
        animals = Animals.objects.all()
        serializer = AnimalsSerializer(animals, many=True)
        response_data = {'animals': serializer.data}
        return Response(response_data, status=status.HTTP_200_OK)

class AnimalsSearchListView(APIView):
    def get(self, request, animals_name):
        try:
            animals_name = animals_name.capitalize()
            animal = Animals.objects.get(name=animals_name)
            serializer = AnimalsSerializer(animal)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Animals.DoesNotExist:
            return Response({'message': 'Animal not found'}, status=status.HTTP_404_NOT_FOUND) 
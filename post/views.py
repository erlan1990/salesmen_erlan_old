from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *

class AutoViewSet(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        # Получаем URL изображения
        photo_url = instance.photo.url
        return Response({'auto': serializer.data, 'photo_url': photo_url})

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        # Получаем URL изображения
        photo_url = instance.photo.url
        return Response({'house': serializer.data, 'photo_url': photo_url})

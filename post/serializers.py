# from rest_framework import serializers
# from .models import *

# class AutoSerializer(serializers.ModelSerializer):
#     # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
#     class Meta:
#         model = Auto
#         fields = "__all__"

# class HouserSerializer(serializers.ModelSerializer):
#     # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
#     class Meta:
#         model = House
#         fields = "__all__"

from rest_framework import serializers
from .models import Auto, House

class AutoSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(use_url=True)  # Включаем поле изображения в сериализацию

    class Meta:
        model = Auto
        fields = '__all__'

class HouseSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(use_url=True)  # Включаем поле изображения в сериализацию

    class Meta:
        model = House
        fields = '__all__'

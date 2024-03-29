from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')
    class Meta:
        model = Comment
        fields = '__all__'
    
    def create(self, validated_data):
        user = self.context.get('request').user
        comment = Comment.objects.create(author=user, **validated_data)
        return comment            


class RatingSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')
    class Meta:
        model = Rating
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        rating = Rating.objects.create(author=user, **validated_data)
        return rating        
    
    # def validate_rating(self, rating):
    #     if not 1 <= rating <= 10:
    #         raise serializers.ValidationError(
    #             'Рейтинг должен быть от 1 до 10'
    #         )
    #     return rating
    
    # def validate_post(self, post):
    #     user = self.context.get('request').user
    #     if self.Meta.model.objects.filter(post=post, author=user).exists():
    #         raise serializers.ValidationError(
    #             'Вы уже оставили отзыв на данный продукт'
    #         )
    #     return post
    

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
from rest_framework import viewsets
from .serializers import *

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # def get_permissions(self):
    #     if self.action in ['list', 'retrieve']:
    #         permissions = [AllowAny]
    #     elif self.action == 'create':
    #         permissions = [IsAuthenticated]
    #     elif self.action in ['update', 'partial_update', 'destroy']:
    #         permissions = [IsAuthorPermission]
        # return [permission() for permission in permissions]


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    # def get_permissions(self):
    #     if self.action in ['list', 'retrieve']:
    #         permissions = [AllowAny]
    #     elif self.action == 'create':
    #         permissions = [IsAuthenticated]
    #     elif self.action in ['update', 'partial_update', 'destroy']:
    #         permissions = [IsAuthorPermission]
    #     return [permission() for permission in permissions]

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
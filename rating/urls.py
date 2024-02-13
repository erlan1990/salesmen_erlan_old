from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, RatingViewSet, LikeViewSet

router = DefaultRouter()
router.register('comments', CommentViewSet)
router.register('ratings', RatingViewSet)
router.register('likes', LikeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
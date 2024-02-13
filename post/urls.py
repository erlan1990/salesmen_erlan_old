from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AutoViewSet, HouseViewSet

router = DefaultRouter()

router.register(r'autos', AutoViewSet)
router.register(r'houses', HouseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

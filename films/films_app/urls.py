from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import FilmViewSet

router = DefaultRouter()
router.register('films', FilmViewSet, basename='films')

urlpatterns = [
    path('', include(router.urls)),
]

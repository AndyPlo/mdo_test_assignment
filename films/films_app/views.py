from django.db.models import Count
from rest_framework import mixins, viewsets

from .models import Film
from .serializers import FilmDetailSerializer, FilmSerializer


class FilmViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Film.objects.annotate(number_of_actors=Count('actors'))

    def get_serializer_class(self):
        if self.action == 'list':
            return FilmSerializer
        return FilmDetailSerializer

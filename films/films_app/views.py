from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets

from .filters import FilmFilter
from .models import Film
from .serializers import FilmDetailSerializer, FilmSerializer


class FilmViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Film.objects.annotate(
        number_of_actors=Count('actors')
    ).order_by('-rating')
    filter_backends = (
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    )
    ordering_fields = ('release_date', 'rating')
    filterset_class = FilmFilter
    search_fields = ('title', )

    def get_serializer_class(self):
        if self.action == 'list':
            return FilmSerializer
        return FilmDetailSerializer

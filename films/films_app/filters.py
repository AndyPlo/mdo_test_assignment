from django_filters import FilterSet, ModelMultipleChoiceFilter

from .models import Film, Genre


class FilmFilter(FilterSet):
    genre = ModelMultipleChoiceFilter(
        field_name='genre__genre',
        to_field_name='genre',
        queryset=Genre.objects.all()
    )

    class Meta:
        model = Film
        fields = '__all__'

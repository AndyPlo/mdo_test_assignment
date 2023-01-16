from rest_framework import serializers

from .models import Actor, Film, SimilarFilm


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('first_name', 'last_name')


class SimilarFilmSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField(source='similar_film.title')
    release_date = serializers.ReadOnlyField(
        source='similar_film.release_date')

    class Meta:
        model = SimilarFilm
        fields = ('title', 'release_date')


class FilmSerializer(serializers.ModelSerializer):
    genre = serializers.ReadOnlyField(source='genre.genre')
    number_of_actors = serializers.IntegerField()

    class Meta:
        model = Film
        fields = ('title', 'rating', 'genre', 'number_of_actors')


class FilmDetailSerializer(serializers.ModelSerializer):
    genre = serializers.ReadOnlyField(source='genre.genre')
    actors = ActorSerializer(many=True)
    similar_movies = serializers.SerializerMethodField()

    class Meta:
        model = Film
        fields = ('title', 'release_date', 'rating',
                  'genre', 'actors', 'similar_movies')

    def get_similar_movies(self, obj):
        similar_movies = obj.similar_films.all()
        return SimilarFilmSerializer(similar_movies, many=True).data

from django.contrib import admin

from . import models


@admin.register(models.Actor)
class ActorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre', 'slug')


@admin.register(models.Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'rating')
    ordering = ['title', 'release_date', 'rating']


@admin.register(models.SimilarFilm)
class SimilarFilmAdmin(admin.ModelAdmin):
    list_display = ('film', 'similar_film')

from django.db import models

from .utils import rating_choices, year_choices


class Actor(models.Model):
    first_name = models.CharField(
        'Имя',
        max_length=50
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=50
    )

    class Meta:
        ordering = ['first_name']
        verbose_name = 'Актеры'
        verbose_name_plural = 'Актеры'
        constraints = [
            models.UniqueConstraint(
                fields=['first_name', 'last_name'],
                name='unique_actor'
            )
        ]

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Genre(models.Model):
    genre = models.CharField(
        'Жанр',
        max_length=50
    )
    slug = models.SlugField(
        'Уникальный слаг',
        max_length=50,
        unique=True,
        null=True
    )

    class Meta:
        ordering = ['genre']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        constraints = [
            models.UniqueConstraint(
                fields=['genre', 'slug'],
                name='unique_genre'
            )
        ]

    def __str__(self):
        return self.genre


class Film(models.Model):
    title = models.CharField(
        'Название',
        max_length=50,
        unique=True
    )
    release_date = models.PositiveBigIntegerField(
        'Год выхода',
        choices=year_choices()
    )
    rating = models.PositiveIntegerField(
        'Рейтинг',
        choices=rating_choices()
    )
    genre = models.ForeignKey(
        Genre,
        verbose_name='Жанр',
        related_name='films',
        on_delete=models.SET_NULL,
        null=True
    )
    actors = models.ManyToManyField(
        Actor,
        verbose_name='Актеры'
    )

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['-rating']

    def __str__(self):
        return self.title


class SimilarFilm(models.Model):
    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE,
        related_name='similar_films',
        verbose_name='Фильм'
    )
    similar_film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE,
        verbose_name='Похожий фильм'
    )

    class Meta:
        ordering = ['film']
        verbose_name = 'Похожий фильм'
        verbose_name_plural = 'Похожие фильмы'
        constraints = [
            models.UniqueConstraint(
                fields=['film', 'similar_film'],
                name='unique_similar_films'
            )
        ]

    def __str__(self):
        return f'{self.film} - {self.similar_film}'

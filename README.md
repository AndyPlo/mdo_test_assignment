# mdo_test_assignment

Тестовое задание для компании "Мой Дом Онлайн".

## Описание задания

### Develop a RESTful web service to obtain movie information.

#### The following information about the movie should be stored in the database:
1. Title
2. Release Date
3. Rating (min value - 1, max value - 5)
4. Genre
5. Actors
6. Similar movies

#### Create API endpoints to get a list of movies and detailed information about a particular movie.

##### The endpoint with collection of movies should return the following:
1. Title
2. Rating
3. Genre
4. Number of actors

Users should be able: 
- to order movies by release date and rating (default ordering by rating DESC)
- filter by genre (multiple) 
- and search by title.

##### The endpoint with detailed information should return the following:
1. Title
2. Release Date
3. Rating
4. Genre
5. Actors (first name, last name)
6. Similar movies (title, release date)

**Задание находится в процессе разработки...**

## Особенности реализации

- Разработка ведется в IDE VSCode с использованием Docker Dev Container (Debian);
- Стек: Django, DjangoRestFramework;

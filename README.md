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

## Особенности реализации

- Разработка велась в IDE VSCode с использованием Docker Dev Container (Debian);
- Стек: Django, DjangoRestFramework;

## Установка и запуск в dev-режиме

1. Установите виртуальное окружение (команда: `python -m venv venv`).
2. Активируйте виртуальное окружение (команда: `source venv/bin/activate`).
3. Установите зависимости из файла requirements.txt (команда: `pip install -r requirements.txt`).
4. Выполните миграции (команда: `python manage.py migrate`).
5. Заполните базу данных (команда: `python manage.py loaddata fixtures.json`).
6. Суперюзер - admin, пароль - admin.
7. Запустите dev-сервер (команда: `python manage.py runserver`).

## Примеры запросов

Request: [GET] http://127.0.0.1:8000/films/?ordering=release_date&genre=Драма&genre=Криминальный&search=Побег

Response:
```json
[
    {
        "title": "Побег из Шоушенка",
        "rating": 5,
        "genre": "Драма",
        "number_of_actors": 2
    }
]
```

Request: [GET] http://127.0.0.1:8000/films/5/

Response:
```json
{
    "title": "Крестный отец",
    "release_date": 1972,
    "rating": 3,
    "genre": "Драма",
    "actors": [
        {
            "first_name": "Аль",
            "last_name": "Пачино"
        },
        {
            "first_name": "Марлон",
            "last_name": "Брандо"
        }
    ],
    "similar_movies": [
        {
            "title": "Криминальное чтиво",
            "release_date": 1994
        },
        {
            "title": "Побег из Шоушенка",
            "release_date": 1994
        }
    ]
}
```

## Автор

Андрей Плотников (Andy.Plo@yandex.ru)

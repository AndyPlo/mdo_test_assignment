import datetime


def rating_choices():
    return [(rating, rating) for rating in range(1, 6)]


def year_choices():
    return [(year, year) for year in range(1900, datetime.date.today().year+1)]

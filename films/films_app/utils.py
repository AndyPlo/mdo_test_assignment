import datetime as d


def rating_choices():
    return [(rating, rating) for rating in range(1, 6)]


def year_choices():
    return [(year, year) for year in range(d.date.today().year, 1900, -1)]

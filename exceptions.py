class NegativeTitlesError(Exception):
    def __init__(self, message):
        self.message = message


def titles_positive(titles):
    if titles < 0:
        raise NegativeTitlesError("titles cannot be negative")


class InvalidYearCupError(Exception):
    def __init__(self, message):
        self.message = message


def year_cup(year):
    world_cup_years = [
        1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974,
        1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022]

    if year not in world_cup_years:
        raise InvalidYearCupError("there was no world cup this year")


class ImpossibleTitlesError(Exception):
    def __init__(self, message):
        self.message = message


def titles_bigger_than_cups(titles, disputed_cups):
    if titles > disputed_cups:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")

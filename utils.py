from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError


def data_processing(seleção: dict):
    titles = seleção.get("titles", 0)

    if titles < 0:
        raise NegativeTitlesError("titles cannot be negative")

    first_cup = int(seleção.get("first_cup")[:4])

    if first_cup < 1930:
        raise InvalidYearCupError("there was no world cup this year")

    cups = []

    for year in range(1930, 2024, 4):
        cups.append(year)

    if first_cup not in cups:
        raise InvalidYearCupError("there was no world cup this year")

    index_first_cup = cups.index(first_cup)
    disputed_cups = cups[index_first_cup:]

    if titles > len(disputed_cups):
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")

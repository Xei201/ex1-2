days_before_month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]


def year_vis(year: int) -> bool:
    """Проверка года на вискос"""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def year_to_day(year: int) -> int:
    """Года в дни с учётом високосных лет"""

    y = year - 1
    return y*365 + y//4 - y//100 + y//400


def month_to_day(month: int, year: int) -> int:
    """Месяцы в дни с учётом високосных лет"""

    day = days_before_month[month - 1]
    if year_vis(year) and month > 2:
        day = day + 1
    return day


def date_to_day(date: str) -> int:
    """Конвертер дат в дни"""

    year, month, day = (int(x) for x in date.split("-"))
    sum_day = year_to_day(year) + month_to_day(month, year) + day
    return sum_day


def date_diff(date_1: str, date_2: str) -> int:
    return abs(date_to_day(date_1) - date_to_day(date_2))






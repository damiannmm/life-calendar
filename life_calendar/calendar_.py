from datetime import date, datetime, timedelta
from textwrap import dedent

from life_calendar import constants


def get_header(weeks=constants.WEEKS_OF_YEAR, years=constants.YEARS_OF_LIFE):
    space = constants.SPACE
    right_space = constants.SPACE

    lweek = len(str(weeks - 1))

    header = space * weeks * lweek

    for idx in range(weeks):
        stop = idx * lweek

        val = idx + 1
        sval = str(val)
        lval = len(sval)
        if val == 1 or (val % 5 == 0 and val > 0):
            header = header[:stop] + sval + header[stop + lval:]

    return header


def count_days(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d').date()
    today = date.today()

    return (today - birthdate).days


def get_matrix(days, weeks=constants.WEEKS_OF_YEAR, years=constants.YEARS_OF_LIFE):
    right_space = constants.SPACE

    matrix = []
    cells = [constants.UNDER for idx in range(weeks * years)]

    axes = days // constants.DAYS_OF_WEEK
    axes -= axes // weeks // constants.DAYS_OF_WEEK  # handling weeks offset  
    slashes = days % constants.DAYS_OF_WEEK
    # unders

    for idx in range(axes):
        cells[idx] = constants.AXE

    if slashes:
        cells[axes] = constants.SLASH

    for year in range(years):
        row = ''
        for week in range(weeks):
            row += cells[week + year * weeks] + right_space
        matrix.append(row)

    return matrix

def add_indent(header, matrix, years=constants.YEARS_OF_LIFE):
    space = constants.SPACE
    left_space = constants.SPACE
    right_space = constants.SPACE

    lyear = len(str(years - 1))
    eindent = left_space + space * lyear + right_space

    calendar = [eindent + header]

    for idx in range(years):
        sval = str(idx)
        lval = len(sval)

        indent = eindent

        if idx % 5 == 0:
            indent = left_space + space * (lyear - lval) + sval + right_space

        calendar.append(indent + matrix[idx])

    return calendar


def main(birthdate, target):
    header = get_header()
    days = count_days(birthdate)
    matrix = get_matrix(days)
    calendar = add_indent(header, matrix)

    sresult = constants.OPEN_SINGLESPACE + constants.NEWLINE

    for row in calendar:
        sresult += row + constants.NEWLINE

    sresult += constants.CLOSE_SINGLESPACE

    with open(target, 'w') as file:
        file.write(sresult)

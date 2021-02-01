from datetime import date, datetime

from life_calendar import constants


def get_header(weeks=constants.WEEKS_OF_YEAR):
    space = constants.SPACE

    lweek = len(str(weeks))

    header = space * weeks * lweek

    for idx in range(weeks):
        val = idx + 1
        sval = str(val)
        lval = len(sval)

        stop = idx * lweek

        if val == 1 or val % 5 == 0:
            header = header[:stop] + sval + header[stop + lval:]

    return header


def count_days(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d').date()
    today = date.today()

    return (today - birthdate).days


def get_matrix(days, weeks=constants.WEEKS_OF_YEAR,
               years=constants.YEARS_OF_LIFE):
    right_space = constants.SPACE

    matrix = []
    cells = [constants.UNDER for idx in range(constants.WEEKS_OF_YEAR * years)]

    axes = days // constants.DAYS_OF_WEEK
    axes -= axes // (weeks * constants.DAYS_OF_WEEK)  # handling weeks offset
    slashes = days % constants.DAYS_OF_WEEK
    # unders

    for idx in range(axes):
        cells[idx] = constants.AXE

    if slashes:
        cells[axes] = constants.SLASH

    for year in range(years * constants.WEEKS_OF_YEAR // weeks):
        row = ''

        for week in range(weeks):
            row += cells[week + year * weeks] + right_space

        matrix.append(row)

    return matrix


def add_indent(header, matrix, weeks=constants.WEEKS_OF_YEAR,
               years=constants.YEARS_OF_LIFE):
    space = constants.SPACE
    left_space = constants.SPACE
    right_space = constants.SPACE

    lyear = len(str(years - 1))
    eindent = left_space + space * lyear + right_space

    calendar = [eindent + header]

    for idx in range(years * constants.WEEKS_OF_YEAR // weeks):
        val = idx * weeks / constants.WEEKS_OF_YEAR
        ival = int(val)
        sval = str(ival)
        lval = len(sval)

        ival_1 = int(val - 1 * weeks / constants.WEEKS_OF_YEAR)

        indent = eindent

        if idx == 0 or (ival % 5 == 0 and ival_1 % 5 != 0):
            indent = left_space + space * (lyear - lval) + sval + right_space

        calendar.append(indent + matrix[idx])

    return calendar


def main(birthdate, target, weeks, years):
    header = get_header(weeks)
    days = count_days(birthdate)
    matrix = get_matrix(days, weeks, years)
    calendar = add_indent(header, matrix, weeks, years)

    open_line = constants.OPEN_SINGLESPACE + constants.NEWLINE
    close_line = constants.CLOSE_SINGLESPACE + constants.NEWLINE

    sresult = ''

    for row in calendar:
        sresult += row + constants.NEWLINE

    sresult = open_line + sresult + close_line

    with open(target, 'w') as file:
        file.write(sresult)

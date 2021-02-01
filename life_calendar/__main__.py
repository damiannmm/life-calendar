from argparse import ArgumentParser

from life_calendar import calendar_, constants

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-b', '--birthdate', type=str, default=None)
    parser.add_argument('-t', '--target', type=str, default=None)
    parser.add_argument('-w', '--weeks', type=int,
                        default=constants.WEEKS_OF_YEAR)
    parser.add_argument('-y', '--years', type=int,
                        default=constants.YEARS_OF_LIFE)

    args = parser.parse_args()

    calendar_.main(args.birthdate, args.target, args.weeks, args.years)

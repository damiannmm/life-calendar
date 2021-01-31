from argparse import ArgumentParser

from life_calendar import calendar_

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-b', '--birthdate', type=str, default=None)
    parser.add_argument('-t', '--target', type=str, default=None)

    args = parser.parse_args()

    calendar_.main(args.birthdate, args.target)

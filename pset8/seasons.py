from datetime import date
from validator_collection import checkers
import inflect
import sys


def main():
    birthday = input("Date of birth: ").strip()
    if not check_input(birthday):
        sys.exit("Invalid date")
    print(to_words(to_minutes(birthday)))


def check_input(birthday):
    if "-" in birthday and checkers.is_date(birthday):
        return True
    else:
        return False


def to_minutes(birthday):
    year, month, day = birthday.split("-")
    difference = date.today() - date(int(year), int(month), int(day))
    return round(difference.days * 24 * 60)


def to_words(minutes):
    p = inflect.engine()
    return f"{p.number_to_words(minutes, andword="").capitalize()} minutes"


if __name__ == "__main__":
    main()

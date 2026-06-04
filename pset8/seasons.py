from datetime import date
import inflect
import sys


def main():
    birthday = input("Date of birth: ").strip()
    try:
        minutes = to_minutes(birthday)
    except ValueError:
        sys.exit("Invalid date")
    else:
        print(to_words(minutes))


def to_minutes(date_of_birth, today=date.today()):
    birthday = date.fromisoformat(date_of_birth)
    if isinstance(today, str):
        t = date.fromisoformat(today)
        difference = t - date(birthday.year, birthday.month, birthday.day)
    else:
        difference = date.today() - date(birthday.year, birthday.month, birthday.day)
    return round(difference.days * 24 * 60)


def to_words(minutes):
    p = inflect.engine()
    return f"{p.number_to_words(minutes, andword="").capitalize()} minutes"


if __name__ == "__main__":
    main()

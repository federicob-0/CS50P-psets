import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(?P<hour1>1[0-2]|0?[1-9])(?P<minute1>:[0-5][0-9])? (?P<meridiem1>am|pm|AM|PM) to (?P<hour2>1[0-2]|0?[1-9])(?P<minute2>:[0-5][0-9])? (?P<meridiem2>am|pm|AM|PM)$"
    if match := re.search(pattern, s):
        meridiem1 = match.group("meridiem1").upper()
        meridiem2 = match.group("meridiem2").upper()

        hour1 = int(match.group("hour1"))
        if hour1 == 12 and meridiem1 == "AM":
            hour1 = 0
        if hour1 != 12 and meridiem1 == "PM":
            hour1 += 12

        hour2 = int(match.group("hour2"))
        if hour2 == 12 and meridiem2 == "AM":
            hour2 = 0
        if hour2 != 12 and meridiem2 == "PM":
            hour2 += 12

        if match.group("minute1"):
            minute1 = match.group("minute1").replace(":", "")
        else:
            minute1 = "00"
        if match.group("minute2"):
            minute2 = match.group("minute2").replace(":", "")
        else:
            minute2 = "00"
    else:
        raise ValueError("Incorrect input")

    return f"{hour1:02}:{minute1} to {hour2:02}:{minute2}"


if __name__ == "__main__":
    main()

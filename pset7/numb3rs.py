import re
import sys


def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if len(sys.argv) == 2:
        print(validate(sys.argv[1]))
    else:
        print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$"
    if re.search(pattern, ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()

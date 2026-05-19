import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r"<iframe.+src=(?:\"|')?(?:http://|https://)?(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)(?:\"|')?.+iframe>"
    if match := re.search(pattern, s):
        return f"https://youtu.be/{match.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()

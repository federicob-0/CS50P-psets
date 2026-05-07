import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    print(count_lines())


def count_lines():
    lines = 0
    try:
        with open(sys.argv[1]) as file:
            reader = file.readlines()
            for row in reader:
                if row.isspace():
                    continue
                elif not row.lstrip().startswith("#"):
                    lines += 1
        return lines
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()

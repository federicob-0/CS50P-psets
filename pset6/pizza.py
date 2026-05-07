import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    print(convert_to_table(sys.argv[1]))


def convert_to_table(csv_file):
    try:
        with open(csv_file) as f:
            reader = csv.reader(f)
            return tabulate(reader, headers="firstrow", tablefmt="grid")
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()

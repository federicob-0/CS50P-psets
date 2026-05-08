import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")

    writecsv(sys.argv[2])


def writecsv(filename):
    with open(filename, "w") as f:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in cleancsv(sys.argv[1]):
            writer.writerow(row)


def cleancsv(filename):
    cleanedfile = []
    try:
        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                last, first = row["name"].split(",")
                row = {"first": first.strip(), "last": last, "house": row["house"]}
                cleanedfile.append(row)
            return cleanedfile
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()

import sys
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid input")
    elif not sys.argv[2].lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid output")
    elif sys.argv[1].rpartition(".")[2] != sys.argv[2].rpartition(".")[2]:
        sys.exit("Input and output have different extensions")

    shirtify(sys.argv[1], sys.argv[2], "shirt.png")


def shirtify(inputfile, outputfile, overlay):
    try:
        with Image.open(inputfile) as img, Image.open(overlay) as shirt:
            new_img = ImageOps.fit(img, (600, 600))
            new_img.paste(shirt, shirt)
            new_img.save(outputfile)
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()

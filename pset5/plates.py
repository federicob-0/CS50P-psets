def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2<= len(s) <=6:
        return False
    if not s.isalnum():
        return False
    if not s[:2].isalpha():
        return False

    found_number = False
    for character in s:
        if character.isdigit():
            if character == "0" and not found_number:
                return False
            found_number = True
        elif found_number and character.isalpha():
            return False

    return True

if __name__ == "__main__":
    main()

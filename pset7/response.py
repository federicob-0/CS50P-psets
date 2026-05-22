from validator_collection import validators, checkers


def main():
    try:
        if checking(input("What's your email address? ")):
            print("Valid")
    except ValueError:
        print("Invalid")


def checking(email):
    valid = validators.email(email)
    return checkers.is_email(valid)


if __name__ == "__main__":
    main()

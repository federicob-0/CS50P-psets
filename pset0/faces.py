def main():
    text = input()
    print(convert(text))

def convert(face):
    return face.replace(":)", "🙂").replace(":(", "🙁")

main()

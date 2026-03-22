def main():
	user_input = input("camelCase: ")
	convert(user_input)
      
def convert(user_i):
	print("snake_case: ", end="")
	for character in user_i:
		if character.isupper():
			print("_" + character.lower(), end="")
		else:
			print(character, end="")
	print()
	
main()

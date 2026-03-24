def main():
	default_input = get_input()
	convert(default_input)
	
def get_input():
	text = input("Input: ")
	return text
		
def convert(default):
	vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
	print("Output: ", end="")
	for letter in default:
		if letter not in vowels:
			print(letter, end="")
						
main()

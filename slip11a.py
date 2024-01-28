#Write a Python program that counts the number of occurrences of a character in a string.

def count_occurrences(string, char):
	count = 0
	for c in string:
		if c == char:
			count += 1
	return count

# Example usage
string = input('Enter a string: ')
char = input('Enter a character: ')
occurrences = count_occurrences(string, char)
print(f"The character '{char}' occurs {occurrences} times in the string.")

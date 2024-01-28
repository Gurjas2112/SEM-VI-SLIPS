#Write a python program to count number of upper case letters, small case letters, digits in the file.

def count_characters(filepath):
	upper_count = 0
	lower_count = 0
	digit_count = 0

	with open(filepath, 'r') as file:
		content = file.read()
		for char in content:
			if char.isupper():
				upper_count += 1
			elif char.islower():
				lower_count += 1
			elif char.isdigit():
				digit_count += 1

	print("Number of uppercase letters:", upper_count)
	print("Number of lowercase letters:", lower_count)
	print("Number of digits:", digit_count)

count_characters('file2.txt')

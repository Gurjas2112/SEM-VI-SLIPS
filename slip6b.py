#Write a Python class which has two methods get_String and print_String.
#get_String accept a string from the user and print_String prints the string in
#upper case. Further modify the program to reverse a string word by word
#and print it in lower case.

class StringManipulator():
	def get_String(self):
		self.string = input("Enter a string: ")

	def print_String(self):
		print(self.string.upper())

	def reverse_and_print(self):
		words = self.string.split()
		reversed_string = ' '.join(reversed(words))
		print(reversed_string.lower())


obj = StringManipulator()
obj.get_String()
obj.print_String()
obj.reverse_and_print()

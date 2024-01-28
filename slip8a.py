#Write a Python program that encrypts a message by adding a key value to every character.

def encrypt_message(message, key):
	encrypted_message = ""
	for char in message:
		encrypted_char = chr(ord(char) + key)
		encrypted_message += encrypted_char
	return encrypted_message

message = input("Enter the message to encrypt: ")
key = int(input("Enter the key value: "))

encrypted_message = encrypt_message(message, key)
print("Encrypted message:", encrypted_message)


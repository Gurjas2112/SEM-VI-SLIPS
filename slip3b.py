#Write a Python program to check if a given key already exists in a
#dictionary. If key exists replace with another key/value pair.

def check_key(d, key):
	if key in d:
		print(key, "already exists in the dictionary")
		new_key = input("Enter new key: ")
		d[new_key] = d[key]
		del d[key]
		print("After replacing key/value pair:", d)
	else:
		print(key, "does not exist in the dictionary")

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
key = int(input("Enter key to check: "))
check_key(d, key)

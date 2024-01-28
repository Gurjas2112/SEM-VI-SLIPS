#Write a python program to reverse a string.

def reverse(s):
	s1=""
	for i in range(len(s)-1,-1,-1):
		s1=s1+s[i]
	return s1
s=input("Enter a string:")
print("Reversed string is:",reverse(s))

#Write a Python script using class to reverse a string word by word.

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

s=input("Enter a string: ")
print("The original string is : ", end="")
print(s)
print("The reversed string(word by word) is : ", end="")
print(reverse(s))

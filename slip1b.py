#Write a python program to accept string and remove the characters which
#have odd index values of given string using user defined function.

s=input("Enter a string:")
def remove(s):
    s1=""
    for i in range(len(s)):
        if i%2==0:
            s1=s1+s[i]
    return s1
print("String after removing odd index values:",remove(s))

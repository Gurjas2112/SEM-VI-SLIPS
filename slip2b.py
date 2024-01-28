#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def count_upper_lower(s):
      upper = 0
      lower = 0
      for ch in s:
         if ch.isupper():
               upper += 1
         elif ch.islower():
               lower += 1
      return upper, lower
a=input("Enter a string:")
print('Number of upper case characters:',count_upper_lower(a))

